'===================================================Декораторы==============================='
# функция высшего порядка - фунция которая принимает в аргументы другую функцию созадет внутри себя функцию вызывает внутри функцию и возвращает функцию
# def func1():
#     ...
#     def func2(a): #функция высшего порядка так как принимает другую функцию в аргументы
#         a()

# func2(func1) 

#Декораторы это функции высшего порядка которая нужна что бы расширить функционал другой функции не изменяя ее(функция обертка)

# def glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func()
#         return text + 'тихо'
#     return wrapper
# @glushitel
# def gun():
#     return 'стреляет'
# result = gun()
# print(result)

from datetime import datetime

def func_start_time(func):
    def wrapper():
        time = datetime.now().stftime('$d.%m.%Y %H:%M')
    print(f'Наша функция запустилась {time_}')
    func()
    return wrapper

func_start_time
def func():
    print('hi')
@func_start_time
def func1():
    print('hello')

func()
func1()
