import requests
from bs4 import BeautifulSoup
from pprint import pprint

class MyError(Exception):
    pass

def weather():
    while True:
        try:
            locate = input('위치를 입력하세요:')
            if locate == '':
                raise MyError
            elif str.isdigit(locate) == True:
                raise MyError
            elif str.isdigit(locate) == False:
                break
        except:
            print('위치를 다시 입력해주세요')
            continue

    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locate}+날씨'
    response = requests.get(url)
    response_code = int(response.status_code)

    if response_code == 200:
        soup = BeautifulSoup(response.content, 'lxml' )
    else:
        print('웹페이지 오류입니다.')
    
    while True:
        try:
            temp = soup.find('div', {'class': 'temperature_text'}).find('strong').text[5:] #현재 온도
            today_chart_list = soup.find('ul',{'class':'today_chart_list'}).select('span',{'class':'txt'}) #미세먼지 초미세먼지 자외선 리스트
            summary_list = soup.find('dl',{'class':'summary_list'}).select('dd',{'class':'desc'}) #강수확률 습도
            before = soup.find('div',{'class':'temperature_info'}).select('p', {'class':'summary'})[0].text #어제 비교
            rainper = summary_list[0].text #강수확률
            waterper = summary_list[1].text #습도
            dust1 = today_chart_list[0].text #미세먼지
            dust2 = today_chart_list[1].text #초미세먼지
            uv = today_chart_list[2].text #자외선
            break
        except:
            print('검색한 위치에 날씨 정보가 없어요.')
            print('-' * 50)
            weather()
    
    
    print('-' * 40)
    print(f'{locate}의 날씨를 불러옵니다')
    print(f'현재온도는 {temp} 입니다.')
    print(f'{before[:-5]}|{before[13:]}')
    print(f'강수확률: {rainper} | 습도: {waterper}')
    print(f'미세먼지: {dust1} | 초미세먼지: {dust2} | 자외선: {uv}')
    print('-' * 40)

weather()