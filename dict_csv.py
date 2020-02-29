import csv
dict = []
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    dict =[
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
    writer = csv.DictWriter(f, dict, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)