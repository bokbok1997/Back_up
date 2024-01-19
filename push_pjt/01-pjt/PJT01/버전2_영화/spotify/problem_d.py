import json
import os
from pprint import pprint

dir_name=os.listdir("data/artists")
def max_polularity(artists):
    # 여기에 코드를 작성합니다.
    global dir_name
    top1=0
    for dir_num in dir_name:
        path = "data/artists/"+dir_num
        people1 = open(path, encoding="utf-8")
        people1_detail = json.load(people1)
        if top1<people1_detail["popularity"]:
            top1 = people1_detail["popularity"]
            artist_name=people1_detail['name']
    return artist_name


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))