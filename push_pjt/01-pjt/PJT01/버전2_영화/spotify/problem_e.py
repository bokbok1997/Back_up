import json
import os
from pprint import pprint
dir_name=os.listdir("data/artists")
def dec_artists(artists):
    # 여기에 코드를 작성합니다.
    global dir_name
    output_list=[]
    for dir_num in dir_name:
        path = "data/artists/"+dir_num
        people1 = open(path, encoding="utf-8")
        people1_detail = json.load(people1)
        if 10000000 <= people1_detail["followers"]['total']:
            cnt = 0
            temp_str=''
            print(people1_detail["uri"])
            for user_id in people1_detail["uri"]:
                if cnt >= 15:
                    temp_str+=user_id
                cnt+=1

            output_list.append({
                'name': people1_detail["name"],
                'uri-id': temp_str
            })
    return output_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint(dec_artists(artists_list))
