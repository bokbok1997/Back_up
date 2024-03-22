
sys.stdin = open('input.txt','r')

import sys
from collections import deque
input = sys.stdin.readline
delta = [(-1,0),(0,-1),(0,1)]
def fff(level,sum_v):
    global res
    if level == 4:
        if res < sum_v:
            res = sum_v
        return
    # for i,j in stack:
    for i in range(len(stack)):
        for di,dj in delta:
            ni,nj=stack[i][0]+di,stack[i][1]+dj
            if 0<=ni<N and 0<=nj<M and check[ni][nj]==0:
                check[ni][nj] = 1
                stack.append((ni,nj))
                fff(level+1,sum_v+arr[ni][nj])
                stack.pop()
                check[ni][nj] = 0

N,M= map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
res = 0
for x in range(M):      # 시작 지점 골라봐
    for y in range(N-1,-1,-1):
        check = [[0] * M for _ in range(N)]
        # stack = [(y,x)]
        stack=deque()
        stack.append((y,x))
        check[y][x] =1
        fff(1,arr[y][x])
print(res)