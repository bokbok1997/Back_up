import sys
sys.stdin = open('input1.txt','r')

# 비트 연산을 이용 => 순서가 다름
# N,M=map(int,input().split())
# for i in range(1,1<<N):
#     stack = []
#     for j in range(N):
#         if i&(1<<j):
#             stack.append(j+1)
#     if len(stack)==M:
#         print(*stack)

def fff(idx,level,stack):
    if level == M:
        print(*stack)
        return
    else:
        for i in range(idx+1,N-(M-level-1)):
            stack.append(i+1)
            fff(i,level+1,stack)
            stack.pop()

N, M = map(int, input().split())
fff(-1,0,[])

