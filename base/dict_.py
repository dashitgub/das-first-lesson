'====================================Словари========================='
'dict - это изменяемый итерируемый неупорядочный(псевдопорядок) неидексируемый тип данных для хранения данных в парах'
#{ключ:значение}

#user = {'name': 'Anonym', 'age': 30,'last_name': 'Makers'}
#print(user['name'])
#print(user['age'])
#print(user['last_name'])

#ключами в словаре могут быть только неизменяемые типы данных
#ключи в словарях должны быть уникальными 

'==================================создание словарей==================================='
#dict_ = {'a':1, 'b':2}

#dict_ = dict([('a',1), ('b', 2)])
#print(dict_)

#dict_ = dict(['a1', 'b2', 'c3'])
#print(dict_) #{'a': '1', 'b': '2', 'c': '3'}
#dict_ = {}
#print(dict_['name'])
#dict_['name'] = 'makers'
#dict_['age'] = 50
#dict_['last_name'] = 'bootcamp'
#print(dict_)

'====================================Методы словаря==================================='

'get - метод, который аолучает значение по ключу, если указанного ключа нету то выходит None - по умолчанию мы можем его поменять'

#user = {
#    'name': 'Anonym', 'age': 15, 'last_name' : 'Makers'
#}

#print(user['id']) #error - KeyError
#print(user.get('id', 'Такого ключа нету')) # None или Такого ключа нету

'pop - удаляет пару по ключу и возвращает значение'

#dict_ = {'a':1, 'b':2, 'c':3}
#popped = dict_.pop('b') 
#print(dict_) # 
#print(popped) #2 

'popitem - удаляет послдение пару и возвращяет ее '
#dict_ = { 'a' : 1, 'b' : 2, 'c' : 3 }
#popped = (dict_)

'update - расширяет словарь парами из второго словоря'

#dict_1 = {1:'a' , 2:'a'}
#dict_2 = {2 : 'b', 3: 'b'}
#dict_1.update(dict_2)
#print(dict_1) #{1: 'a', 2: 'b', 3: 'b'}

#'clear - очищает словарь'
#dict_ = {'a' : 1, 'b':2, 'c' : 3}
#dict_.clear()
#print(dict_) # {}

'fromkeys -  метод для создания нового словоря использую  список ключей'

#dict_ = dict.fromkeys('hi')
#print(dict_) #{'h': None, 'i': None}
#dict_2 = dict.fromkeys(['hi', 123, True])
#print(dict_2) #{'hi': None, 123 : None, True:0}

#'keys, values, items
#keys - метод который возвращает все ключи
#values - метод который возвращает все значения
#items-  метод который возвращает пары ключи и значения в виде tuple

#user = {
 #   'name':'Anonym', 'age': 15, 'last_name' : "makers"
#}
#print(user.keys()) #['name', 'age', 'last_name'])
#print(user.values()) #['Anonym', 15, 'makers'])
#print(user.items()) #[('name', 'Anonym'), ('age', 15), ('last_name', 'makers')])

'=====================================Итерирование словарей========================================='
#user = {
#    'name':'Anonym', 'age': 15, 'last_name' : "makers"
#}

#for key in user:
#    print(key)
# при итерации словоря будут приходить ключи
#for value in user:
#    print(value)
#при итерации словоря с методом values(), приходят значения

#for item in user.items():
#    print(item)
#при итерации словоря с методом items(), приходит tuple с ключем и значением

#for k, v in user.items():
#    print(f'Ключ{k}, значения{v}')
#при итерации словоря с методом items() приходит  tuple  с ключем и значением

dict_1 = {1 : 'a', 2 : 'b'}
dict_2 = {}
for k, v in dict_1.item():
    dict_a[v] = k
print(dict_2)
