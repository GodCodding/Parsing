import requests
from bs4 import BeautifulSoup
import json
import sys

URL = 'https://www.mebelshara.ru/contacts'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0','accept':'*/*'}
info=[]
def get_html(url,params=None):
    r=requests.get(url,headers=HEADERS,params=params)
    return r

def get_content(html):
    soup=BeautifulSoup(html, 'html.parser')
    list_city=soup.find_all('div',class_='city-item')
    list_information=soup.find_all('div',class_='shop-list')

    for city in list_city:
        info.append({
            'city':city.find("h4",class_="js-city-name").get_text(strip= True),
        })
        for information in list_information:
            info.append({
                'address':city.find('div',class_='shop-address').get_text(strip= True),
                'worktime':city.find('div',class_='shop-weekends').get_text(strip= True)
            })
def parse():
    try:
        html=get_html(URL)
        get_content(html.text)
        json.dumps(info)
        print(info)
    except Exception:
        print("Error occuried during web request!")
        print(sys.exc_info()[1])

parse()
