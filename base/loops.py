'====================================Циклы=================================='
'цикл - это бллок кода который повторяет код несколько раз'
'есть два вида цикла'
# 1)For - цикл который работает с итерируемым обьектом.Цикл заканчивает работу когда доходит до последнего элемента итерируемого обьекта
# 2) While - цикл который работает до тех пор пока условие верное(True) 
'Итерируемый обьект - это какая то последовательность, например: Лист является итерируемым обьектом.[1,2,3,4,5,], string - (dasss)  (123,True, ,1 ,5) dict, set'

'Итерация - процесс перебора итерируемого обьекта(когда мы по очерди вытаскиваем элементы в последовательности)'
'------------------------------------------------------------------------------------------------------------------------------------------------------------------'

'for'
#list_ = [12, 'hi', True, None, [0,0,0]]
#for i in list_:
#    print(i)

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------'
#for number in [12, 3, 4, 0, -1, 20]:
 #   print(number * 2)

#for i in [2, 12, 5, 3]:
 #   print(i ** 2)

'----------------------------------------------------------------------------------------------------'
#text = 'makers'
#for i in text:
#    print(i) 

'---------------------------------------------'
#list_ = [2, 5, 20, 10, 9,-1]
#for i in list_:
 #   if i % 2:
#        print(i)

#list_ = [2, 5, 20, 10, 9,-1]
#for i in list_:
#    if i % 2 == 0:
#        print(i)
    

#n = 1 
#while n < 10:
 #   print(n)
 #   n = n + 1
'=========================================Ключевые слова в циклах======================================================='
# break - это принудительное остановка кода(цикла) 
# continue - пропускает итерацию, продолжает с новой(следующей) итерации

#range() #генератор
#for i in range(1, 11):
#    if i == 3:
#        continue
#    print(i)

#for i in range(11):
#    print(i)
#    break
##0
#for i in range(11):
#    if i == 2:
#        break
#    print(i)
#n = 1
#while n > 10:
#    if n == 2:
#        continue
#    print(n)

n = 0 
while n < 10:
    print(n)
    if n > 100:
        break
    n += 1 #n = 1 + 1
