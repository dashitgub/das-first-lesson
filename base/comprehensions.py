'==========================Comprehensions==============='
# генератор с помощью которого можно создать последовательность используя for в одну строку
#результат for элемент in последовательность
# list_1 =[x + 2 for x in range(11)]
# print(list_1) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# list1 = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)

# list_ = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list_.append('четный')
#     else:
#         list_.append('нечетный')
# print('list_')


# list_ = ['четный' if i % 2 == 0 else 'нечетный' for i in range(1,11)] #['нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный']
# print(list_) #['нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный']

'если в comprehension можно добовлять условия там их бывает два вида'
'1 - тернарный оператор пишется перед циклом так как используется и if и else'
'2 - фильтр пишется после цикла так как используется только if'

# list1 = [12, True, None, 'hi', 0, False, 'makers', 'world']
# list2 = [item for item in list1 if isinstance(item, str)]

# print(list2)

'=========================Виды comp====================='
'1 - list comprehension'
'2 - dict comprehension'
'3 - set comprehension'
'Dict comprehension'
# dict_1 = {i:i**2 for i in range(1,11)}
# print(dict_1)

# dict_1 = {'a': 1, 'b': 2, 'c': 300}
# dict_2 = {value: i for i, value in dict_1.items()}
# print(dict_2)


# dict_1 = {
#     'a': [1, 2, 3], 
#     'b': [12, 0, 1], 
#     'c': [32, 0, 0, 10]
#     }
# dict_2 = {}

# for k, value in dict_1.items():
#     dict_2[k] = sum(value)
# for k, value in dict_2.items():
#     print(f"Сумма значений списка {k}: {value}")

'set comprehension'

# set_1 = {i for i in range(1,11)}
# print(set_1) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set_1 = {i for i in 'makers'}
# print(set_1)

# set_1 = {2,3,4,15,1}
# set_2 = {i**i for i in set_1} #{4,27,126, ,1}
# print(set_2)

# set_1 = {12, 4, 34, 5, 6}
# set_1_str = {str(num) for num in set_1}
# print(set_1_str)

'сохрвните только строки'
set_1 = {1, 12, 'hi', 34, True, 'makers'}
set_2 = {e for e in set_1 if isinstance(e, str)}
print(set_2)

'создайте словарь где ключи будут числа от 1 до 5 а значениями списки с числами от 1 до этого числа'

dict_1 = {i: [for i in range(1,i+1)] for i in range(1,6)}
print(dict_1)
