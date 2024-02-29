def fff(loc,res):
    global min_v
    if res > min_v: return
    if sum(visited) == N-1:
        min_v = res + arr[loc][0]
        return
    for i in range(1,N):
        if loc == i or visited[i] == 1:
            continue
        visited[i] = 1
        fff(i,res+arr[loc][i])

        visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_v = 100000
    visited = [0]*N
    fff(0,0)
    print(f'#{tc+1} {min_v}')

