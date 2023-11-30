# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_student = {}
for student in students:
    if student['first_name'] in count_student:
        count_student[student['first_name']] += 1
    else:
        count_student[student['first_name']] = 1
for name, count in count_student.items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
counter_student_name_max = {}
for students_dict in students:
    if students_dict['first_name'] in counter_student_name_max:
        counter_student_name_max[students_dict['first_name']] += 1
    else:
        counter_student_name_max[students_dict['first_name']] = 1

name = max(counter_student_name_max.items(), key=lambda item: item[1])

print(f'Самое частое имя среди учеников: {name[0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

def max_count_name(school_class):
    counter_student_name_max = {}
    for students_dict in school_class:
        if students_dict['first_name'] in counter_student_name_max:
            counter_student_name_max[students_dict['first_name']] += 1
        else:
            counter_student_name_max[students_dict['first_name']] = 1
    name_student = max(counter_student_name_max.items(), key=lambda item: item[1])
    return name_student[0]


for number_class, school_class in enumerate(school_students, start=1):
    max_count_name_student = max_count_name(school_class)
    print(f'Самое частое имя в классе {number_class}: {max_count_name_student}')
    


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def student_counting(students):
    counter_gender_student = {'men': 0, 'female': 0}
    for student_dict in students:
        if is_male[student_dict['first_name']] is True:
            counter_gender_student['men'] += 1
        else:
            counter_gender_student['female'] += 1
    return counter_gender_student



for classes in school:
    students = classes['students']
    class_num = classes['class']
    count_gend_stud = student_counting(students)
    print(f'Класс {class_num}: девочки {count_gend_stud["female"]}, мальчики {count_gend_stud["men"]}')
    

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

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
def student_counting(students):
    counter_gender_student = {'men': 0, 'female': 0}
    for student_dict in students:
        if is_male[student_dict['first_name']] is True:
            counter_gender_student['men'] += 1
        else:
            counter_gender_student['female'] += 1
    if counter_gender_student['men'] > counter_gender_student['female']:
        return True 
    else:
        return False 



for classes in school:
    students = classes['students']
    class_num = classes['class']
    count_gend_stud = student_counting(students)
    
    if count_gend_stud is True:
        print(f'Больше всего мальчиков в классе {class_num}')
    else:
        print(f'Больше всего девочек в классе {class_num}')