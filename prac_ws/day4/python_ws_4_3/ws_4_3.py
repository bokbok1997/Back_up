import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()



# 특정 데이터 출력
dummy_data=[]
for cnt in range(10):
    if (-80<(float(parsed_data[cnt]['address']['geo']['lat'])) < 80):
        if (80>float(parsed_data[cnt]['address']['geo']['lng']) > -80):
            temp={
                'company' : parsed_data[cnt]['company']['name'],
                'lat' : parsed_data[cnt]['address']['geo']['lat'],
                'lng' : parsed_data[cnt]['address']['geo']['lng'],
                'name' : parsed_data[cnt]['name']
            }
            dummy_data.append(temp)

print(dummy_data)

