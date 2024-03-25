'==================================Exceptions=========================='
#Исключения это обьекты который прерывают код если не было обработки 

'SyntaxError,- ошибка которое выходит при синтактической ошибке'
'Example: a = .(no value) SyntaxError'
'---------------------------------------------------------------------------------------------'
'NameError - выходит когда вы обращаетесь к несуществуюещему обЬекту(переменной)'
'Example: num1 = 15 print(num5)'
'---------------------------------------------------------------------------------------------'
'IndexError - исключение которое выходит когда мы обращаемся по не сущ. индексу'
'Exampl: list_ = [12,2,3,0] print(list_[1000])' 

# [12,0,24,'hi'].pop(1000)
# IndexError:pop ondex out of range

# [].pop()
# IndexError: pop from rmpt list
'------------------------------------------------------------------------------------------------'
'KeyError - исключение которое выходит когда мы обращаемся по не сущ ключу'
#Ошибки не будет т.к метод get не вызывает ошибку а вернет None
# dict_ = {'a': 1}
# dict_['c']
'--------------------------------------------------------------------------------------------------'
'ValueError - это исключение выходит когла мы передаем функци. не корект для нее тип данных'
#второй случай когда мы распаковывваем итеррируемый обьект на несколько переменных и кол во этих  переменных не совпадает с кол во этих переменных 

# int('10sdjsd')
# ValueError

# a, b = 1 , 2 ,3 
#Value Error
'-----------------------------------------------------------------------------------------------------'
'TypeError '
#Исключение выходит, когда мы пытаемся использовать методы не свойственны кокому то типу данных
#так же выходит когда мы пытаемся передать функцию больше или меньше аргументов чем принимает сама функция
 
# for i in 12312: 
#     ...
#     TypeError
#     ...

'''
"5" + 5
TypeError
'''
'-------------------------------------------------------------------------------------------------------------'
ZeroDivisionError
'''
45 / 0
ZerodivisionError
'''
'''
45 % 0
ZeroDivisionError
'''
'AttributeError, когда мы обращаемся к не сущ атрибуту или методу обьекта данных (типа данных)'
# [1,23,1,56]
AttributeError
'''
'makers'. pop(0)
AttributeError
'''

'IdentationError'
'''
IdentationError
for i in range(11):
print(i)
IdentationError - нету отступов Табуляции
'''
Exception
#исключение которое создали что бы его вызывать

'===================================Вызов Исключений========================='

'принудительный призыв через raise'
# raise NameError('ТЫ ЛОХ')

'==============================Обработка Исключений========================'
#Оработка исключений нужна что бы код не прекращал работу мы можем использовать конструкци. Try-except и обрабатывать вызванное исключение
# try: #код который может вызвать исключение(ошибку)
#     num = int(input('Введите число: '))
# except ValueError: #Ловим ошибку на ошибке #Обрабоотку на исключение которое поймали
#     print('Вы ввели не число!') 
# else:#код который обработает если исключение не вышло
#     print('Вы ввели число {num}')
# finally: #работает всегда
#     print('ДО свидания')


# try:
#     num = input("Введите число :")
#     res = 10 / num
# except (ValueError, ZeroDivisionError):
#     print("Что-тo пошло не так!")

#except: обрабатывает все исключения которые могут выйти
#except Exception - 
    
#можем указать в except несколько исключений при помощи скобок и запятой except {ValueError,TypeError}
    
try:
    number = int(input("Введите число: "))
    
    if number > 0:
        raise ValueError("Положительные числа вызывают ValueError")
    elif number < 0:
        raise TypeError("Отрицательные числа вызывают TypeError")
    elif number == 0:
        raise ZeroDivisionError("0 вызывает ZeroDivisionError")
    
except ValueError as ve:
    print("Ошибка:", ve)
except TypeError as te:
    print("Ошибка:", te)
except ZeroDivisionError as zde:
    print("Ошибка:", zde)
except Exception as e:
    print("Необработанная ошибка:", e)  