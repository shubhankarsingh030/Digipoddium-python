import requests
import pandas as pd
from bs4 import BeautifulSoup

def get (url):
    page =  requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.text, 'lxml')
    else:
        print('Error: ', page.status_code)
        return None


def extract(soup):
    target = soup.find('div', class_="_1YokD2 _3Mn1Gg")
    products = target.find_all('div', class_="_1AtVbE col-12-12")   
    print('products:', len(products))
    info = []
    for item in products:
        name = item.find('div',class_='_4rR01T')
        s_price = item.find('div',class_='_30jeq3 _1_WHN1')
        o_price = item.find('div',class_='_3I9_wc _27UcVY')
        rating = item.find('div',class_='_3LWZlK')  
        rating_count = item.find('div',class_='_2_R_DZ')
        data = {}
        try:
            data['name'] = name.text.string()
        except:
            data['name'] = None
        try:
            data['s_price'] = s_price.text.string()
        except:
            data['s_price'] = None
        try:
            data['o_price'] = o_price.text.string()
        except:
            data['o_price'] = None
        try:
            data['rating'] = rating.text.string()
        except:
            data['rating'] = None
        try:
            data['rating_count'] = rating_count.text.string()
        except:
            data['rating_count'] = None
        info.append(data)
        print('Extracted: ' , name.text)
    return info         

def save(data):
    if len(data_list) > 0:
            pd.DataFrame(data_list).to_csv('headlines.csv', index = False)
    else:
            print('No data to save')

def main():
    pos = 1
    product = 'tv'
    datalist = []
    while True:
        url = "https://www.flipkart.com/search?q={product}tv&page={pos}"
        print(url)
        soup = get(url)
        if soup:
            data = extract(soup)
            if data:
                datalist.extend(data)
                pos = 1
            else:
                break
        else:
            break
            

main()
    
