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

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
data_list=list(map(create_user,name,age,address))
print(data_list)
