import requests
from bs4 import BeautifulSoup
from pprint import pprint

def covid19():
    url1 = "http://ncov.mohw.go.kr/"
    url2 = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    response1 = requests.get(url1)  # get 방식으로 웹 정보 받아오기
    response2 = requests.get(url2)
    response_code = int(response1.status_code)  # 응답 코드 받기

    if response_code == 200:  # 정상 작동(코드 200 반환) 시
        soup1 = BeautifulSoup(response1.content, 'lxml')
        soup2 = BeautifulSoup(response2.content, 'lxml')
    else:  # 오류 발생
        print("웹 페이지 오류입니다.")
    
    
    comfirmed_list = soup1.find("div", {"class": "occur_num"}).select('div', {'class': 'box'}) #누적 확진자 리스트
    today_list1 = soup2.find_all('dd', {'class': 'ca_value'})
    today_list2 = soup2.find('tr', {'class': 'sumline'}).select_one('td')
    
    confirmed = comfirmed_list[1].text[6:-4].replace(',','') #누적 확진자 수
    today1 = today_list1[6].text #국내 발생
    today2 = today_list2.text #해외유입
    
    today1 = today1.replace(',','')
    today2 = today2.replace(',','')
    
    print("|국내 코로나 확진자 수 현황|")
    print("http://ncov.mohw.go.kr/ 의 정보를 가져옵니다.")
    print(f"일일 확진자 총: {int(today1) + int(today2):,}명 | 국내발생: {int(today1):,}명 | 해외유입: {int(today2):,}명")
    print(f"누적 확진자 {int(confirmed):,}명")

covid19()



