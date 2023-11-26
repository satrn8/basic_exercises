# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
def count_student():
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'}
    ]

    counts = {}
    for student in students:
        if student["first_name"] not in counts.keys():
            counts[student["first_name"]] = 1
        else:
            counts[student["first_name"]] += 1

    for student, count in counts.items():
        print(f"{student}: {count}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
def popular_name():
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]

    counts = {}
    for student in students:
        if student["first_name"] not in counts.keys():
            counts[student["first_name"]] = 1
        else:
            counts[student["first_name"]] += 1

    max_count = max(counts, key=counts.get)
    print(f"Самое частое имя среди учеников: {max_count}, оно встречается {counts.get(max_count)}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

def popular_name_students():
    school_students = [
        [  # это – первый класс
            {'first_name': 'Вася'},
            {'first_name': 'Вася'},
        ],
        [  # это – второй класс
            {'first_name': 'Маша'},
            {'first_name': 'Маша'},
            {'first_name': 'Оля'},
        ], [  # это – третий класс
            {'first_name': 'Женя'},
            {'first_name': 'Петя'},
            {'first_name': 'Женя'},
            {'first_name': 'Саша'},
        ],
    ]

    count = 0
    for school in school_students:
        counts = {}
        for student in school:
            if student["first_name"] not in counts.keys():
                counts[student["first_name"]] = 1
            else:
                counts[student["first_name"]] += 1
        count += 1

        max_count = max(counts, key=counts.get)
        print(f"Самое частое имя среди учеников {count} класса: {max_count}, оно встречается {counts.get(max_count)}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

def count_boy_and_girl():
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

    for cl in school:
        boy = 0
        girl = 0
        for student in cl["students"]:
            for name in student.values():
                if is_male[name]:
                    boy += 1
                else:
                    girl += 1
        print(f"Класс {cl['class']}: девочки {girl}, мальчики {boy} ")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

def class_comparison():
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

    for cl in school:
        boy = 0
        girl = 0
        for student in cl["students"]:
            for name in student.values():
                if is_male[name]:
                    boy += 1
                else:
                    girl += 1

        if girl > boy:
            print(f"Больше всего девочек в классе {cl['class']}")
        elif boy == girl:
            print(f"Девочек и мальчиков одинаковое количество в классе {cl['class']}")
        else:
            print(f"Больше всего мальчиков в классе {cl['class']}")


if __name__ == "__main__":
    count_student()
    popular_name()
    popular_name_students()
    count_boy_and_girl()
    class_comparison()