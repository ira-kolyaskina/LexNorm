import random

def select_random_from_chunks(lst):
    selected = []
    for i in range(0, len(lst), 4):
        chunk = lst[i:i+4]
        selected.extend(random.sample(chunk, min(3, len(chunk))))
    return selected

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    return content.split('\n\n') 


path = "/home/irina/git/LexNorm/data/unchecked_markup/OLOLO.txt"
data = read_file(path)
result = select_random_from_chunks(data)
# print(result)

with open("/home/irina/git/LexNorm/data/unchecked_markup/OLOLO20k.txt", 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(result))