from collections import Counter
# Задание 1

# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [

  {'first_name': 'Вася'},

  {'first_name': 'Петя'},

  {'first_name': 'Маша'},

  {'first_name': 'Маша'},

  {'first_name': 'Петя'},

]

print('Задание 1')
stl = []
for i in students:
    stl.append(i.get('first_name'))
count_stl = Counter(stl)
for k,v in count_stl.items():
    print(k+': '+str(v))


# Пример вывода:

# Вася: 1

# Маша: 2

# Петя: 2





# Задание 2

# Дан список учеников, нужно вывести самое часто повторящееся имя.

students = [

  {'first_name': 'Вася'},

  {'first_name': 'Петя'},

  {'first_name': 'Маша'},

  {'first_name': 'Маша'},

  {'first_name': 'Оля'},

]
print('Задание 2')
stl = []
for i in students:
    stl.append(i.get('first_name'))
count_stl = Counter(stl)
for k,v in count_stl.items():
    if v == max(count_stl.values()):
        print('Самое частое имя среди учеников: ', k)

# ???

# Пример вывода:

# Самое частое имя среди учеников: Маша



# Задание 3

# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.

school_students = [

  [  # это – первый класс

    {'first_name': 'Вася'},

    {'first_name': 'Вася'},

  ],

  [  # это – второй класс

    {'first_name': 'Маша'},

    {'first_name': 'Маша'},

    {'first_name': 'Оля'},

  ]

]

# ???
print('Задание 3')
stl = []
for num in range(len(school_students)):
    for i in school_students[num]:
        stl.append(i.get('first_name'))
    count_stl = Counter(stl)
    for k,v in count_stl.items():
        if v == max(count_stl.values()):
            print('Самое частое имя в классе', ': ', k)
    stl = []    
    count_stl=[]


# Пример вывода:

# Самое частое имя в классе 1: Вася

# Самое частое имя в классе 2: Маша





# Задание 4

# Для каждого класса нужно вывести количество девочек и мальчиков в нём.

school = [

  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},

  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},

]

is_male = {

  'Маша': False,

  'Оля': False,

  'Олег': True,

  'Миша': True,

}

# ???
print('Задание 4')
stl = []
for i in school:
    for j in i.get('students'):
        stl.append(j.get('first_name'))
    m=0
    w=0
    for k in range(len(stl)):
        if is_male[stl[k]]:
            m += 1
        else:
            w += 1
    print('в классе', i.get('class'), w, ' девочек и ', m, 'мальчиков') 
    stl = []    
    count_stl=[]


# Пример вывода:

# В классе 2a 2 девочки и 0 мальчика.

# В классе 3c 0 девочки и 2 мальчика.





# Задание 5

# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

school = [

  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},

  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},

]

is_male = {

  'Маша': False,

  'Оля': False,

  'Олег': True,

  'Миша': True,

}

# ???

print('Задание 5')
stl = []
man = []
woman = []
dict_all = []
m= 0
w = 0
man_c = {}
woman_c = {}
for i in school:
    for j in i.get('students'):
        stl.append(j.get('first_name'))
    for k in stl:
        if is_male[k]:
            man.append(k)
        else:
            woman.append(k)

    dict1={"Класс": i.get('class'),"Мальчики":len(man), "Девочки": len(woman)}
    dict_all.append(dict1)
    man =[]
    woman =[]
    stl = []    
    count_stl=[]
print(dict_all) 
for l in dict_all:
    if l.get('Мальчики') > m:
       m = l.get('Мальчики') 
       man_c = l.get('Класс')
    if l.get('Девочки') > w:
       w = l.get('Девочки') 
       woman_c = l.get('Класс')  
print('Больше всего мальчиков в классе ', man_c)   
print('Больше всего девочек в классе ', woman_c) 

# Пример вывода:

# Больше всего мальчиков в классе 3c

# Больше всего девочек в классе 2a