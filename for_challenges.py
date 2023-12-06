# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

def print_name():
    names = ['Оля', 'Петя', 'Вася', 'Маша']
    for name in names:
        print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4


def print_name_and_len():
    names = ['Оля', 'Петя', 'Вася', 'Маша']
    for name in names:
        print(f"{name}, количество букв в имени {len(name)}")


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика


def print_name_and_gender():
    is_male = {
        'Оля': False,  # если False, то пол женский
        'Петя': True,  # если True, то пол мужской
        'Вася': True,
        'Маша': False,
    }
    names = ['Оля', 'Петя', 'Вася', 'Маша']

    for name in names:
            if is_male[name] == False:
                print(f"{name} женский пол")
            else:
                print(f"{name} мужской пол")


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.


def print_group_and_student_len():
    groups = [
        ['Вася', 'Маша'],
        ['Вася', 'Маша', 'Саша', 'Женя'],
        ['Оля', 'Петя', 'Гриша'],
    ]
    print(f"Количество групп {len(groups)}")
    count = 1
    for group in groups:
        print(f"Группа {count}: {len(group)} ученика")
        count += 1


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша


def print_students_groups():
    groups = [
        ['Вася', 'Маша'],
        ['Оля', 'Петя', 'Гриша'],
        ['Вася', 'Маша', 'Саша', 'Женя'],
    ]
    count = 1
    for student in groups:
        student = ', '.join(student)
        print(f"Группа {count}: {student}")
        count += 1


if __name__ == "__main__":
    print_name()
    print_name_and_len()
    print_name_and_gender()
    print_group_and_student_len()
    print_students_groups()
