list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
book_cnt=len(rental_list)
for a in rental_list:
    cnt =0
    for b in list_of_book:
        if a == b:
            cnt+=1
    if cnt == 0:
        print(f'{a} 은/는 보유하고 있지 않습니다.')
        break
    else:
        book_cnt -=1
if book_cnt == 0:
    print('모든 도서가 대여 가능한 상태입니다.')
