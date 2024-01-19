"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""
import json
import os
from pprint import pprint

dir_name=os.listdir("data/artists")

def get_popular():
    # 여기에 코드를 작성합니다.
    global dir_name
    output_list=[]
    for dir_num in dir_name:
        temp={}
        path = "data/artists/"+dir_num
        people1 = open(path, encoding="utf-8")
        people1_detail = json.load(people1)
        if 5000000 <= people1_detail["followers"]['total'] <= 10000000:
            print(people1_detail["name"])
            temp['followers']=people1_detail["followers"]['total']
            temp['name']=people1_detail["name"]
            output_list.append(temp)

    return output_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
