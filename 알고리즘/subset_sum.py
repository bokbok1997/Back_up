# 부분집합 중 원소의 합을 구하는 문제
# 완전검색 기법으로 모든 부분집합을 만들고 합을 구해본다

# bit = [0,0,0,0]
# for i in range(2):
#     bit[0]=i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 # print(bit)
#                 if sum(bit)>=3:
#                     print(bit)

def f(arr,N):
    temp = []
    for i in range(1<<N):
        for j in range(N):
            if i&(1<<j):
                print(arr[j],end="," )

            print()
        print()

    # if s == 0:
    #     return True
    return 0

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

f(arr,12)
