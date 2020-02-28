from collections import Counter
# Вывести последнюю букву в слове
word = 'Архангельск'
print('Последняя буква: ' + word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
count=Counter(word.lower())
print('Букв а в слове:',count['а'])

# Вывести количество гласных букв в слове
word = 'Архангельск'
print([word.lower().count(v) for v in "аеёиоу"])
s=sum(word.lower().count(v) for v in "аеёиоу")
print('Гласных в слове:',s)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words=sentence.split()
print(words)
print('Количество слов в предложении:',len(words))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words=sentence.split()
for word in words:
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sum_len=0
for number in range(len(words)):
    sum_len+=len(words[number])
print(sum_len/len(words))