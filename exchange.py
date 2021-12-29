import requests
from bs4 import BeautifulSoup
from pprint import pprint

def exchange():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'
    response = requests.get(url)
    response_code = int(response.status_code)

    if response_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')

    else: 
        print('웹 페이지 오류')

    ex = soup.find('tbody').select('td')
    Time = soup.find('p', {'class' : 'grp_info'}).text
    bank = soup.find('span', {'class' : 'radio_text'}).text

    USD = ex[0].text
    USDPM = ex[2].text

    JPY = ex[3].text
    JPYPM = ex[5].text

    EUR = ex[6].text
    EURPM = ex[8].text

    CNY = ex[9].text
    CNYPM = ex[11].text

    print(f'{bank} - 매매기준율 ({Time[1:17]})')
    print(f'USD/KRW = {USD}원 등락률 {USDPM}')
    print(f'JPY100/KRW = {JPY}원 등락률 {JPYPM}')
    print(f'EUR/KRW = {EUR}원 등락률 {EURPM}')
    print(f'CNY/KRW = {CNY}원 등락률 {CNYPM}')


exchange()
    



