# string1 = 'строка с одинаковыми ковычками'
# string2 = "строка с двойными ковычками"
# string3 = "don't"  # Внутри двойных кавычек все одинарные кавычки-просто часть текста
# string4 = 'название магазина Азбука'
# string5 = ''''''''
# # многострочный текст в одинарных кавычках. Тут можно исползовать и одинарные и двойные
# string7 = 'hello'
#
#
#
# '==============экранизация строк============'
# '\n' #перенос на новую строку
# print('hello world') #hello world
# '-----------------------------------'
# print('hello \n world') #hello #world
# '------------------------------------'
# print('he\nllo world') #he llo world
# '--------------------------------------'
# '\t' #Табуляция (несколько пробелов)
# print('hello\tworld') #hello           world
# print('he\tllo world') #he   llo world
#
# '\v' #перенос на нову. строку со смещением вправо на длинну предыдущей строки
#
# print('hello\vworld') # hello
#                               #world
# '\r' #перенос каретки в самое начало
# print('hello world\rMa') #Mallo world
#
# print('home\Makers')
# '\''  #отабражение одинарной ковычки
# "\'" #отабражение двойных ковычек
# '\\' # отабражение \
# print('комманда \n - переносит строку')
#
# '=======================форматирование строк================='
# title = 'Iphon15'
# price = 1000
# shop = 'makers'
# # print('Я купил title за price $')
#
# '1) f- строка'
# print(f' Я купил {title} за {price}$, в магазине {shop}')
#
# '2) %s'
# print('я купил %stitle за %sprice $' %(title, price))
#
# '3. str.format'
# print('Я купил {} за {} $ в магазине {}' .format
#       (title, price, shop))
# '=======================Методы строк(str)======================'
# # Методы это функции которые относятся к опеределенному типу данных(классу)
# #к ним мы обращаемся через точку
import errno

# print(dir(str))
# string = 'Hi'
# print(string.upper()) #HELLO WORLD
# print(string.lower()) # hello world
# print(string.swapcase()) #hello WORLD
# print(string.title()) #Hello World
# print(string.capitalize()) #Hello world
# print(string .islower) # True
# print(string.isupper) #False
#
#
# print(string.center(12,'*')) # '      hi        '
# print(string.count('l'))
# print(string.count('el'))
# print(string.count('o'))
# print(string.count('h'))
# print(string.count('Hello'))
#
# print(string.startswith('h')) # true
# print(string.startswith('H')) # true
# print(string.startswith('hello')) # true
# print(string.endswith('ld')) # true
#
# print (string.isalpha)

string = '12345absdefghij'
print(string.isalpha()) #True, Проверяет на буквы
print(string.isdigit()) #true or false проверяет на числа

print(string.isalnum()) #Проверяет является ли строка числом или юуквой или и числом и буквой если есть символ то вернет False
string = 'hello world makers bootcamp'
print(string.split()) ['hello', 'world', 'makers' 'bootcamp']


print(string.replace('h', 'm'))
string = 'h e l l o'
print(string.strip())

'========================================Индексы==================================='
#Индексы это порядковый номер элемента в последовательности (индекс начинается с 0)
#-10-9-8-7-6-5-4-3-2-1
'hello world'
#012345678910
print(string[0]
# print((string[-1]))
# print(string[5])

#срез [start:end(не включительно):step]
print(string[6:10]) #worl
print(string[:5]()) #hello
print(string[::2]) #hlowrd
print(string[::-1])#dlrow ooleh
print(string[::-2]) #drwolh
