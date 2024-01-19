number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people+=1
    pass

def create_user(name,age,address):
    user_info={}
    increase_user()
    user_info['name']=name
    user_info['age']=age
    user_info['address']=address
    print(user_info['name'],end="님")
    print(" 환영합니다!")
    return user_info

print("현재 가입 된 유저 수 : ",number_of_people)
data_1=create_user('홍길동','30','서울')

print(data_1)
print("현재 가입 된 유저 수 : ",number_of_people)