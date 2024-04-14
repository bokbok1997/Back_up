import sys
sys.stdin = open('sample_input.txt','r')

'''
1767. 프로세서 연결하기

가장자리에 있는 코어들까지 리스트에 담은 경우
1,357 ms/82,336 kb
가장자리에 있는 코어들은 리스트에 담지 않은 경우 --> 시간,메모리 상당히 많이 준다
286 ms/53,560 kb
'''


from collections import deque
def fff(core_idx,res,open_cnt):
    global line,open_min
    if open_cnt>open_min:return
    if core_idx == core_num:
        if open_min == open_cnt:
            line = min(line,res)
        else:
            open_min = open_cnt
            line = res
        return

    x,y=core[core_idx][0],core[core_idx][1]
    if x==0 or x==N-1 or y == 0 or y ==N-1:
        fff(core_idx+1,res,open_cnt)
    stack = deque()
    cnt = 0
    for k in range(y+1,N):
        if visited[x][k]!=0:
            break
        else:
            visited[x][k] = 1
            cnt+=1
            stack.append(k)
    else:
        fff(core_idx+1,res+cnt,open_cnt)
    while stack:
        j = stack.pop()
        visited[x][j]=0

    cnt = 0
    for k in range(0, y):
        if visited[x][k] != 0:
            break
        else:
            visited[x][k] = 1
            cnt += 1
            stack.append(k)
    else:
        fff(core_idx + 1, res + cnt,open_cnt)
    while stack:
        j = stack.pop()
        visited[x][j] = 0

    cnt = 0
    for k in range(x + 1, N):
        if visited[k][y] != 0:
            break
        else:
            visited[k][y] = 1
            cnt += 1
            stack.append(k)
    else:
        fff(core_idx + 1, res + cnt,open_cnt)
    while stack:
        i = stack.pop()
        visited[i][y] = 0

    cnt = 0
    for k in range(0, x):
        if visited[k][y] != 0:
            break
        else:
            visited[k][y] = 1
            cnt += 1
            stack.append(k)
    else:
        fff(core_idx + 1, res + cnt,open_cnt)
    while stack:
        i = stack.pop()
        visited[i][y] = 0
    fff(core_idx + 1, res, open_cnt + 1)

T = int(input())
for tc in range(T):
    N=int(input())
    visited = [list(map(int,input().split())) for _ in range(N)]
    core = []
    core_num=0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    continue
                core_num += 1
                core.append((i,j))
    open_min = core_num
    line = core_num*N
    fff(0,0,0)
    print(f'#{1+tc} {line}')