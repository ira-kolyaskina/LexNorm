import csv

with open('raw_RUS_DATA.csv', 'r', encoding='utf-8') as csvfile, open('raw_RUS_DATA.txt', 'w', encoding='utf-8') as txtfile:
    reader = csv.reader(csvfile)
    for row in reader:
        text = row[0][2:-2]
        words = text.split()
        for word in words:
            txtfile.write(f"{word}\t\n")
            
        txtfile.write("\n")
