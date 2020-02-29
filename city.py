import csv
with open('city.csv', 'w', encoding='utf-8', newline='') as f:
    for line in f:
        line = line.upper()
        print(line)