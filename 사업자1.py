import requests
from requests.models import cookiejar_from_dict
class MyError(Exception):
    pass

def workernumber():
    while True:
        try:
            workernum = input('사업자등록번호입력:')
            if workernum == '':
                raise MyError
            elif str.isdigit(workernum) == True:
                break
            elif str.isdigit(workernum) == False:
                raise
        except:
            print('사업자번호를 다시 입력하세요')
            continue
    
    
    headers = {
    'accept': 'application/xml',
    'Authorization': 'AbR7Rrz1WF5IuVD337qUepkGeC1IWCsgiZOObBLbaL/BTu0PKhZsztyez+bo/kdLWMbX8xXO0/e9QlAjm8PpVw==',
    'Content-Type': 'application/json',
    }

    params = (
    ('serviceKey', 'AbR7Rrz1WF5IuVD337qUepkGeC1IWCsgiZOObBLbaL/BTu0PKhZsztyez+bo/kdLWMbX8xXO0/e9QlAjm8PpVw=='),
    )   

    data = f'{{ "b_no": [ "{workernum}" ]}}' 
    
    response = requests.post('https://api.odcloud.kr/api/nts-businessman/v1/status', headers=headers, params=params, data=data).json()
    datalst=response.get('data')
    dict=datalst.pop()
    print(dict.get('b_stt'))
    print(dict.get('tax_type'))
    
        


workernumber()