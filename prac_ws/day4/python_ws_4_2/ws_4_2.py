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
    dummy_data.append(parsed_data[cnt]['name'])
print(dummy_data)
