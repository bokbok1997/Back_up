import json
from pprint import pprint


def artist_info(artist, genres):
    # 여기에 코드를 작성합니다.
    temp={
        "genres_name" : artist["genres_ids"],
        'id' : artist["id"],
        'images' : artist["images"],
        'name' : artist["name"],
        'type' : artist["type"]
        
    }
    gen_ids=artist["genres_ids"]
    for gen in genres:
        for i in range(len(artist["genres_ids"])):
            if gen['id'] == artist["genres_ids"][i]:
                temp['genres_name'][i]=gen['name']
    return temp


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))


