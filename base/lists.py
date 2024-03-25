		'==============================================List======================================='
#списки - изменяемый индексируемый упорядоченный итерируемый тип данных
#предназначенный для хранения любых данных в определенном порядке

#list_1 = [1, 2, 14, 'das', True, [0,0,0], None]
#Index  #0  #1  #2   #3    #4      #5     #6
#list_1 = [3] 
#list1 = [-1] #none
#list_1 = [-2] [-1] #0
#list_1 = [3][-2] #l
#list_1 [5] #[0,0,0] 

'range(start, end(ну выключительная), step) - это функция генератор которая создает диапазон от start до end (не включительно)'

#list('hello') -> [h,e,l,l,o]
#list_2 = list(range(0, 101 ))
#print(list_2)
#print(list(range(50, 101)))

#print(list(range(0, 11, 2)))
#[0, 2, 4, 6, 8, 10]
#[0,2,4,6,8,10] шаг 2
#[0,3,6,9] шаг 3
#[10,9,8,7,6,5,4,3,2,1,0] шаг -1

'============================================методы списков======================================='

# append - добавления элементов в конец списка
#list_ = []
#list_.append(1)
#list_.append('hello world')
#list_.append(True)
#print(list_)

'pop - удаление элемента из списка по индексу, так же возвращает удаленный элемент, Eсли не указать индекс то удалит с конца'

#list_ = [90, True, None, 'hi']
#poped = list_.pop(1)
#print(list_) #all element
#print(poped) #remove element

'remove - удаление элемента из списка по значению'
#list_ = [1, 2, 3, 4, 5, 99, 0, 11]
#list_.remove(5)
#print(list_)

'count - считает кол во принятого элемента в списке'

#list_ = ['Hi'1,23,1,4,5,6,1,'Hi'7,1,'Hi'7,8,1]
#print(list_.count(1)) #5
#print(list_.count(7)) #2

'index - возвращает индекс первого вхождения принятого элемента'
list_ = ['hi', 1, 123, 123, 'makers', 21123, 124234, 212, 1212112312312]
print(list_.index('makers')) 


'extend - расширяет список при помощи другого списка'
list_1 = [1,2,3]
list_2 = [0,0,0]
list_1.append(list_2) #[1,2,3,[0,0,0]]
print(list_1)
list_1.extend(list_2) #[1,2,3,0,0,0]
print(list_1)

'reverse - изменяет список раставляя его элементы в обратном порядке'

list_ = ['hi', 1,2,3, True]
list_.reverse()
print(list_) #[True, 3,2,1,'hi]

'sort - сортирует список состоящий из одного типа данных'
list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_.sort(reverse=True)
print(list_)

list_ = ['c', 'wqd', 'qwdqdqdas']
list_.sort()
print(list_)

'clear - полностью очищает весь лист'

list_ = [12,1124134,1212341 24, ' asjdhnjsdnajsdn']
list_.clear()


'множественное присвоение'
#a ,b ,c = 10, 5 ,2 #a = 10 b = 5 c = 2


#list_ = [23, 'hi', 4, 0, 'makers']
#for i in list_:
#    print(i)

meshok = ['potato', 'onion','potato', 'onion','potato', 'onion']
for ruka in meshok:
    print(ruka)

paket1 = []
paket2 = []

for ruka in meshok:
    if ruka == 'potato':
        paket1.append(ruka)
    elif ruka == 'onion':
        paket2.append(ruka)

print(paket1)
print(paket2)
