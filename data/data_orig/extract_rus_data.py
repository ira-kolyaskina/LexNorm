import zipfile
# import tarfile
import bz2
import json
from tqdm import tqdm as tq
# import gzip 
import glob
import os
import csv
from zipfile import ZipFile


def save_tweets(tweets, filename):  
    csvfilename = filename[47:-4]+'.csv'
    with ZipFile(filename, 'w') as zipfile:
        with open(csvfilename, mode='x', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix', delimiter='\n')
            writer.writerow(tweets)
        zipfile.write(csvfilename)
        os.remove(csvfilename)
            
def extract_tweets_from_file(myfile):
    tweets = []
    content = bz2.decompress(myfile.read())
    for line in content.decode('utf8').split('\r\n'):
        if not line.strip():
            continue
        try: 
            data = json.loads(line.strip())
            in_russian = 'lang' in data and data['lang'] == 'ru' 
            is_retweet = 'retweeted_status' in data
            if in_russian and not is_retweet:
                tweets.append([data['text']])
        except:
            print('json parsing error: ')
    return tweets
    
def extract_tweets_for_day_from_zip(path):
    tweets = []
    with zipfile.ZipFile(path, 'r') as myzip:
        tweet_dumps = [filename for filename in myzip.namelist() if 'json.bz2' in filename]
        for filename in tq(tweet_dumps, desc='Parsing ' + path.split('/')[-1], leave=False):
            with myzip.open(filename, 'r') as myfile:
                extracted_tweets = extract_tweets_from_file(myfile)
                tweets.extend(extracted_tweets)
    return tweets


def extract_tweets_with_location_for_month(directory, path):
    if not os.path.exists(directory):
        os.makedirs(directory)
    archive_file_paths_zip = sorted(glob.glob(path+"*.zip", recursive=True))
    print(archive_file_paths_zip)
    if len(archive_file_paths_zip) != 0:
        for file_path in tq(archive_file_paths_zip, desc='Parsing *.zip'+path.split('/')[-2]):
            name = file_path.split('/')[-1].split('.')[0]
            tweets = extract_tweets_for_day_from_zip(file_path)
            save_tweets(tweets, directory+'/'+name+'_full_ru.zip')
            print('saved: ' + name)



extract_tweets_with_location_for_month(
	'twitter-stream-2021-06-11',
	'/home/irina/Desktop/thesis/data/twitter/',
)
