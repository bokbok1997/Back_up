# 01_-_pjt_ver2_spotify

1. 이번 pjt 통해서 배운점 
* os 라는 모듈의 listdir을 사용해서 특정 디렉토리 내부의 파일 명을 리스트로 받아서 각각 접근하여 사용 할 수 있었다
```dir_name=os.listdir("data/artists")```


* 리스트와 딕셔너리들이 복잡하게 이용되는 데이터를 순서대로 접근해서 읽어 볼 수 있었다 


2. 어려웠던 부분 
* 처음에 여러개로 나누어진 파일에 각각 접근해서 사용자 데이터를 받아오는 과정에서 시간이 많이 소요되었다. 기존에 사용하지 않았던 모듈을 import 해서 사용 하는 작업이 익숙하지 않있다

```python
dir_name=os.listdir("data/artists")
def dec_artists(artists):
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
    return output_lis```