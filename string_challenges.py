# Вывести последнюю букву в слове
def last_letter():
    word = 'Архангельск'
    print(f"Последняя буква в слове '{word}' - {word[-1]}")


# Вывести количество букв "а" в слове
def count_a():
    word = 'Архангельск'
    count_a= 0
    for i in word.lower():
        if i == "а":
            count_a += 1
    print(f"Количество 'a' в слове '{word}' - {count_a}")


# Вывести количество гласных букв в слове
def count_vowels():
    word = 'Архангельск'
    vowels = set("ауоыэяюёие")
    count_vowels = 0
    for i in word.lower():
        if i in vowels:
            count_vowels += 1
    print(f"Количеcтво гласных букв в слове '{word}' - {count_vowels}")


# Вывести количество слов в предложении
def count_words():
    sentence = 'Мы приехали в гости'
    count = sentence.split()
    print(f"количество слов в предложении '{sentence}' - {len(count)}")


# Вывести первую букву каждого слова на отдельной строке
def first_letter():
    sentence = 'Мы приехали в гости'
    first = sentence.split()
    for i in first:
        print(f"Первая буква каждого слова на отдельной строке '{sentence}' - {i[0]}")


# Вывести усреднённую длину слова в предложении
def middle_words():
    sentence = 'Мы приехали в гости'
    middle = sentence.replace(" ", "")
    count_word = 0
    for i in sentence.split():
        count_word += 1
    print(f"Усредненная длина слова в предложении '{sentence}' - {len(middle)/count_word}")


if __name__ == '__main__':
    last_letter()
    count_a()
    count_vowels()
    count_words()
    first_letter()
    middle_words()