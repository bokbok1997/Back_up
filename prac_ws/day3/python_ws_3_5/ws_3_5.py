number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name,age,address):
    user_info={}
    increase_user()
    user_info['name']=name
    user_info['age']=age
    user_info['address']=address
    print(user_info['name'],end="님")
    print(" 환영합니다!")
    return user_info

many_user=list(map(create_user,name,age,address))


def decrease_book(book):
    global number_of_book
    number_of_book-=book
    print(f'남은 책의 수 : {number_of_book}')
    return number_of_book

def rental_book(info):
    book_limit=info['age']//10
    decrease_book(book_limit)
    pass

cnt1=0
for number_of_people in range(5):
   many_user[cnt1]=create_user(name[number_of_people],age[number_of_people],address[number_of_people])
   cnt1+=1
   number_of_people+=1
cnt2=0
for number_of_people in range(5,0,-1):
    rental_book(many_user[cnt2])
    print(many_user[cnt2]['name'],end='님이 ')
    print(many_user[cnt2]['age']//10,end='권의 책을 대여하였습니다.\n')
    cnt2+=1
    number_of_people-=1