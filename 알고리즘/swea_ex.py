import sys
sys.stdin = open("input.txt", "r")

T= int(input())
for tc in range(1, T + 1):
    N,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        cnt_x, cnt_y = 0, 0
        for j in range(N):
            if data[i][j]==1:
                cnt_x += 1
                if j == N-1 and cnt_x == K:
                    res += 1
                    cnt_x = 0
                    # print(i,j)

            else:
                if cnt_x == K and data[i][j-1]==1:
                    res += 1
                    # print(i, j)
                cnt_x = 0

            if data[j][i]==1:
                cnt_y += 1
                if i == N-1 and cnt_y == K:
                    res += 1
                    cnt_y = 0
                    # print(j, i)

            else:
                if cnt_y == K and data[j-1][i]==1:
                    res += 1
                    # print(j, i)
                cnt_y = 0



    print(f'#{tc} {res}')

