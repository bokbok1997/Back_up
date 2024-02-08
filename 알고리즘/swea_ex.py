import sys
sys.stdin = open("sample_in.txt", "r")


def dfs(list,s,g):
    visited.append(s)
    while 1:
        for i in range(1,V+1):
            if arr[s][i] == 1:
                visited.append(i)



    return visited

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
    S, G = map(int, input().split())
    stack = []
    visited=[]
    # print(f'#{tc} {func(S, G)}')
