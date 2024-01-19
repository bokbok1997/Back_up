food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
cnt = 0
while cnt!=3:
    if food_list[cnt]['이름'] == '토마토':
        food_list[cnt]['종류'] = '과일'
    elif food_list[cnt]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(food_list[cnt]['이름'],end=' 은/는 ')
    print(food_list[cnt]['종류'],end=' (이)다\n')
    cnt+=1
print(list(map(lambda x:x , food_list)))
#완료