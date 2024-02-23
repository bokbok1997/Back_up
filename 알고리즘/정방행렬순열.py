def f(i,k,s):
    global min_v
    if i == k:
        if min_v > s:
            min_v = s
        elif s>=min_v:
            return
    else:
        for j in range(i,k):
            p[i],p[j]=p[j],p[i]         # p[i]<->p[j]
            f(i+1,k,s+arr[i][p[i]])
            p[i], p[j] = p[j], p[i]     # 교환 전으로 복구

T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    p=[i for i in range(N)]
    min_v = 100
    f(0,N,0)
    print(f'#{tc} {min_v}')