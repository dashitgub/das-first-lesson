'============================JSON================================='
'Java Script Object Notation - универсальный формат в котором мы храним данные в типах данных понятный почти для всех языков программирования'
import json

# json_list = "[1,2,3,4,5]"
# python_list = json.loads(json_list)
# print(python_list)

# json_data = "null"
# python_data = json.loads(json_data)
# print(python_data)

# json_data = "true"
# python_data = json.loads(json_data)
# print(python_data)

'Десериализация - это перевод с json на питон обьект'
#loads - метод для десереализации с json строки 
#load - метод для десериализиции с json файла

# json_data = 'false'
# python_data = json.loads(json_data) #False
'-----------------------------------------'
# json_data = null
# python_data = json.loads(json_data) #None
'Сериализация - перевод с python в json обьект'
#dumps - метод для серелизации с python в json строку 
#dump - метод для серелизации с python в json файл

# with open('file.json', 'r') as file:
#     python_data = json.load(file)
#     print (python_data)

# python_data =  True
# json_data = json.dumps(python_data)
# print(json_data)

# puthon_data = None
# json_data = json.dumps(python_data)
# print(json_data)

# python_data = {12,4,2,5,6}
# json_data = json.dimps(python_data) #Eror типа данных сет в json в формате не сущ

with open('file2.json', 'w') as file:
    python_data = [12,3,4,1, None, False, True,
                   {1:"hello", 2:'hi'}]
    json.dump(python_data, file)
    
