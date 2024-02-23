def fff(arr):
    tmp = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] < arr[1][1]:
                tmp+=1
    if tmp>3:
        return 1
    else:
        return 0
di = [1,1,1,0,0,-1,-1,-1]
dj = [-1,1,0,-1,1,0,-1,1]
dx=[0,0]
dy=[-1,1]
T = int(input())
for tc in range(T):
    calc = 0
    N,M=map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    temp = [[0]*3 for _ in range(3)]
    arr1=[[0]*2 for _ in range(3)]
    arr2=[[0]*3 for _ in range(2)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            temp[1][1]=data[i][j]
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                temp[1 + di[k]][1 + dj[k]]=data[ni][nj]
            calc+=fff(temp)
    for a in range(1,M-1):
        for x in range(5):
            f1,f2 = 0 + di[k], a + dj[k]
            b1,b2= N-1 + di[-1*(k+1)],a + dj[-1*(k+1)]
            arr2[1][a]=data[][]