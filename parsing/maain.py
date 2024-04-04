'''
1. получить html  код страницы
2 получить карточки с товарами из html кодa
3 распарсить данные из карточки (стянуть данные из карточек)
4 получить данные и записать файл csv
'''
import csv
import requests
from bs4 import BeautifulSoup as BS

URL = 'https://enter.kg/computers/noutbuki_bishkek'

def get_html(URL):
    html = requests.get(URL)
    return html.text


def get_cards(html):
    soup = BS(html, 'lxml')
    laptops = soup.find_all('div', class_ = 'row')
    return laptops

def get_data(list_):
    data = []
    for laptop in list_:
        data.append({
            'title':laptop.find('span', class_ ='prouct_name'), 'price': laptop.find('span', class_ ='price').text, 'image' : 'https://enter.kg/' + laptop.find('img').get('src')
        })
    return data

def get_last_page(html):
    soup = BS(html, 'lxml')
    links = soup.find_all('a', class_ ='pagenav')
    link = links[-1]
    if link.text == 'В конец':
        return True
    else:
        return False

def main(URL):
    count = 0
    while True:
        url = URL +f'/results,{count}01-{count}00'
        html = get_html(url)
        laptops = get_cards(html)
        data = get_data(laptops)
        with open('file.cvs', 'w', encoding = 'utf8') as file:
            writer = csv.DictWriter(file, fieldnames = ['title', 'price', 'image'])
            writer.writeheader()
            for i in data:
                writer.writerow(i)
        flag = get_last_page(html)
        if not flag:
            break    
        count += 1
        print(f'Пасинг старницы {count}')
        
main(URL)
