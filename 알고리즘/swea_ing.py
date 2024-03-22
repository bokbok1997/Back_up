import sys
sys.stdin=open('input1.txt','r')



T = int(input())
for tc in range(T):
    N,B=map(int,input().split())
    S = list(map(int,input().split()))
    dif = B
    for i in range(1,1<<N):
        res = 0
        for j in range(N):
            if i&(1<<j):
        #         print(S[j],end=' ')
        # print()
                res+=S[j]
        print(res)
        dif=min(dif,abs(B-res))
    print(f'#{tc+1} {dif}')