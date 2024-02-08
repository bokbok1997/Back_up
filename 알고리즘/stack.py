# ------스택 문제풀 때 사용한것 현살적인 중복 제거 ------
# def passf(list):
#     temp=[]
#     for i in list:
#         if temp:
#             if i == temp[-1]:
#                 temp.pop()
#             else:
#                 temp.append(i)
#         else:
#             temp.append(i)
#     return temp
# for tc in range(1, 11):
#     N,arr = input().split()
#     N=int(N)
#     print(f'#{tc} {"".join(passf(arr))}')
# ---------------------------------------------------



# def push(item,size):
#     global top
#     top+=1
#     if top==size:
#         print('오버플로우')
#     else:
#         stack[top]=item
#
# def pop():
#     global top
#     if top == -1:
#         print('언더플로우')
#         return 0
#     else:
#         top-=1
#         return stack[top+1]
#
# size = 10
# stack=[0]*size
# top=-1
#
# push(11,size)
# top+=1
# stack[top]=20
# print(stack)
# print(pop())
# if top>-1:
#     top-=1
#     print(stack[top+1])

# -----------------------------------------------------------------
# -------------스택 코드2----------------------------------------

def push(n):
    global top
    top+=1
    if top ==size:
        print('Overflow!')
    else:
        stack[top] = n



top = -1
size = 10
stack = [0]*size  # 최대 10개 push

top+=1          # push(10)
stack[top]=10
top+=1          # push(20)
stack[top]=20
push(30)

while top>-1:
    top-=1
    print(stack[top+1])