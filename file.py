content ={}
with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print('Длина файла: ', len(content))
    print('Количество слов: ', len(content.split()))

    print(content.replace(".","!"))