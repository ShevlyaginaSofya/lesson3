# Задание 1

# Необходимо вывести имена всех учеников из списка с новой строки
print('Задание 1')
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)
print('Второй вариант:')
print('\n'.join(names))
# Задание 2

# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.
names = ['Оля', 'Петя', 'Вася', 'Маша']
print('Задание 2')
name_lengs = {}
for name in names: 
    name_lengs[name] = len(name)
name_lengs = {name: len(name)  for name in names}
print(name_lengs)

print('Второй вариант:')
for name in names: 
    print(name,len(name))

# Задание 3

# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика



is_male = {

  'Оля': False,  # если True, то пол мужской

  'Петя': True,

  'Вася': True,

  'Маша': False,

}

names = ['Оля', 'Петя', 'Вася', 'Маша']

# ???
print('Задание 3')
for name in names:
    if is_male[name]==False:
        print(name,'Женский')
    else:
        print(name,'Мужской')


# Задание 4

# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней

# Пример вывода:

# Всего 2 группы.

# В группе 2 ученика.

# В группе 3 ученика.



groups = [

  ['Вася', 'Маша'],

  ['Оля', 'Петя', 'Гриша'],

]

# ???
print('Задание 4')
print('Всего ',len(groups),' группы')
for number in range(len(groups)):
    print('В группе ',len(groups[number]),' ученика')



# Задание 5

# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.

# Пример:

# Группа 1: Вася, Маша

# Группа 2: Оля, Петя, Гриша



groups = [

  ['Вася', 'Маша'],

  ['Оля', 'Петя', 'Гриша'],

]

# ???
print('Задание 5')
for number in range(len(groups)):
    print(len(groups))
    print(range(len(groups)))
    print('Группа ', number+1,':',", ".join(groups[number]))

