'''
서로소 집합 이해해 보기
'''

def find_set(x):
    while x!=p[x]:
        x=p[x]
    return x

def union(a,b):
    p[find_set(b)] = find_set(a)

def find_set_r(x):              # 참고
    if x==p[x]:
        return x
    else:
        p[x]=find_set_r(p[x])       # path compression
        return p[x]

T = int(input())
for tc in range(1,1+T):
    N,M = map(int,input().split())
    arr =list(map(int,input().split()))
    p=[i for i in range(N+1)]
    for i in range(M):
        a,b=arr[i*2],arr[i*2+1]
        union(a,b)
    cnt = 0
    for i in range(1,1+N):
        if i==p[i]:     # 대표원소인 경우
            cnt+=1      # 대표원소 개수 == 그룹의 수
    print(f'#{tc} {cnt}')