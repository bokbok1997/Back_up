import json
from pprint import pprint


def artist_info(artists, genres):
    temp_list=[]
    for artist in artists:
        temp={
            'genres_name' : artist["genres_ids"],
            'id' : artist["id"],
            'images' : artist["images"],
            'name' : artist["name"],
            'type' : artist["type"]
            }

        for gen in genres:
            for i in range(len(artist["genres_ids"])):
                if artist["genres_ids"][i]==gen['id'] :
                    temp['genres_name'][i]=gen['name']

        temp_list.append(temp)
    return temp_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
