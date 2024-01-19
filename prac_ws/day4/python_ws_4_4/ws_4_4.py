import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

censored_user_list={}

def create_user(user_list):
    global censored_user_list
    for i in range(len(user_list)):
        if (user_list[i]['company']['name']=='Romaguera-Crona')or(user_list[i]['company']['name']=='Yost and Sons')or(user_list[i]['company']['name']=='Robel-Corkery')or(user_list[i]['company']['name']=='Abernathy Group'):
            continue
        else:
            key1=user_list[i]['company']['name']
            val1=[]
            val1.append(user_list[i]['name'])
            tf =censorship(user_list[i])
            if tf == True:
                censored_user_list[key1]=val1
    return censored_user_list


def censorship(id):
    if id['company']['name'] in black_list:
        aaa=id['company']['name']
        bbb=id['name']
        print(f'{aaa}소속의 {bbb}은/는 등록할 수 없습니다')
        return False
    else:
        print('이상 없습니다.')
        return True






print(list(create_user(parsed_data)))


