import requests
from bs4 import BeautifulSoup
from pprint import pprint

class MyError(Exception):
    pass

def weather():
    while True:
        try:
            print('-' * 50)
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

    if response_code == 200: #웹사이트 접속 오류 감지
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
            weather()

    temper = temp[:-1] #온도 기호자르기
    tempint = int(temper)
    
    print('-' * 50)
    print(f'{locate}의 날씨를 불러옵니다')
    print(f'현재온도는 {temp} 입니다.')
    print(f'{before[:-5]} |{before[12:]}')
    print(f'강수확률: {rainper} | 습도: {waterper}')
    print(f'미세먼지: {dust1} | 초미세먼지: {dust2} | 자외선: {uv}')
    print('-' * 50)

    #옷
    if tempint < 5:
        print('추워요 패딩을 입으세요')
    elif 4 < tempint < 9:
        print('코트를 입으세요')
    elif 8 < tempint < 17:
        print('자켓을 입으세요')
    elif 16 < tempint < 20:
        print('얇은니트를 입으세요')
    elif 19 < tempint < 23:
        print('얇은가디건을 입으세요')
    elif 22 < tempint < 28:
        print('반팔을 입으세요')
    elif 27 < tempint:
        print('민소매를 입으세요')
    #마스크
    if dust1 == '좋음':
        print('미세먼지가 적어요 마스크를 안써도 돼요')
    elif dust1 == '보통':
        print('미세먼지가 보통이에요 마스크는 안껴도 될거 같아요')
    elif dust1 == '나쁨':
        print('기관지가 약한 사람은 마스크를 쓰세요')
    elif dust1 == '매우나쁨':
        print('마스크를 꼭 쓰고 물을 자주 섭취하세요')
    print('-' * 50)
     
weather()