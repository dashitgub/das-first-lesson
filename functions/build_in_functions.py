'=======================Встроенные функции====================='

#map, filtre,reduse,zip,enumerate
'ZIP - соединяет несколько последовательностей (получаем генератор в котором элементы - tuple)'

# list1 = [1,2,3,4]
# list2 = ['a', 'b', 'c', 'd']
# list3 = [10.5, 20.6, 35.8, 0.5]

# ziiped = zip(list1, list2, list3)

# for i in ziiped:
#     print(i)


# zipped = zip(list, list2)
#print(list(zipped)) list[tuple, tuple, tuple]
# print(dict(zipped)) dict{k:v, k:v, k,v}

'ENUMERATE - нумерует последовательность (по дефолоту с 0) (тоже возвращает генератор)'

# enumerated = enumerate('hello') #<enumerate object at 0x7f32c31ee500>
# print(list(enumerated)) #[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# for i in enumerated:
    # print(i)

# enum = enumerate([12, 8, 'hi', True, 'hello', None], 15 )
# print(list(enum))

# for i in enum:
#     print(i)

# 'MAP -  принимает другую функцию и последовательность, мэп применяет функцию, которую передали на каждыф элемент из последовательности. Возвращает map генератор'
# list_ = [1,2,3,4] #
# def func(a):
#     return str(a)

# mapped = map(func, list_)
# print(mapped) #
# print(list(mapped)) #['1', '2', '3', 4']

# list_1 = [1,2,3,4]
# def func(a):
#     return a ** 2

# mapped = map(func, list_1)
# print(list(mapped))

'lambda - это одноразовая анонимная функция'

# def func(num):
#     return num ** 3

# func(2) 
# result = ((lambda num: num ** 3) (2))
# print(result(2))

'filter - принимает другую функию и последовательность применет функи. которую мы передали на каждой жлемент последовательности и оставляет только те элементы который прошли проверку'


list_1 = [1,2,3,4,5,6,7,8]
filtered = list(filter(lambda x: x % 2 == 0, list_1))
print(filtered) #[0, 39, 23, 1, 0]

'REDUCE - принимает функцию и последовательность возвращает 1 результат (передеаваемая функция должна принимать 2 аргкмента)'

from functools import resuce

list_1 = [12,3,0,5]
reduce(lambda a, b: a + b, list_1)
print()
