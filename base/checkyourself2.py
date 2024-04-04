1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 3)
print("Результат сложения:", result)
"""

2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""
def print_argument_types(arg1, arg2):
    print("Тип первого аргумента:", type(arg1))
    print("Тип второго аргумента:", type(arg2))

print_argument_types(5, "Hello")

"""
3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers_list = [2, 3, 4, 5]
product = multiply_numbers(numbers_list)
print("Произведение чисел в списке:", product)

"""
4) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
"""
def count_letters(string):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    consonants = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}
    vowels_count = 0
    consonants_count = 0
    other_count = 0

    for char in string.lower():
        if char in vowels:
            vowels_count += 1
        elif char in consonants:
            consonants_count += 1
        else:
            other_count += 1

    print("Количество гласных букв:", vowels_count)
    print("Количество согласных букв:", consonants_count)
    print("Количество остальных символов:", other_count)

string = "Пример строки для теста"
count_letters(string)

"""
5) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""
from functools import reduce

names = ["Александр", "Елена", "Михаил", "Ольга", "Дмитрий"]

longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)
print("Самое длинное имя из списка:", longest_name)
"""
6) Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.
"""
num = 3

def mul():
    global num
    num = num ** 2
    return num

# Вызываем функцию три раза
for _ in range(3):
    mul()

print(num)

"""
7) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
main_matryoshka_size = 10

def add_second_matryoshka(main_size):
    second_matryoshka_size = 5
    return main_size + second_matryoshka_size

def add_third_matryoshka():
    third_matryoshka_size = 3
    size_with_second_matryoshka = add_second_matryoshka(main_matryoshka_size)
    return size_with_second_matryoshka + third_matryoshka_size

result_size = add_third_matryoshka()

print("Итоговый размер матрешек:", result_size)

"""
8) Cоздайте переменную list_ и сохраните в ней список из чисел. Создайте новый список, используя встроенные функции, состоящий из квадратов этих чисел, результат сохраните в новой переменной result и выведите в консоль.
"""
# Создаем список из чисел
list_ = [1, 2, 3, 4, 5]

# Используем map() с lambda-функцией для создания нового списка, состоящего из квадратов чисел
result = list(map(lambda x: x ** 2, list_))

# Выводим результат в консоль
print("Список квадратов чисел:", result)

"""