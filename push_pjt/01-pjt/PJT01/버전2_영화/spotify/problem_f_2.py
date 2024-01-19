"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
import os
from pprint import pprint

dir_name=os.listdir("data/artists")

def acoustic_artists():
    # 여기에 코드를 작성합니다.
    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)
    for gen in genres_list:
        if gen['name'] == "acoustic":
            acoustic_num=gen['id']
    global dir_name
    output_list=[]
    for dir_num in dir_name:
        path = "data/artists/"+dir_num
        people1 = open(path, encoding="utf-8")
        people1_detail = json.load(people1)
        if acoustic_num in people1_detail['genres_ids']:
            output_list.append(people1_detail['name'])
    return output_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())
