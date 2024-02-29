di = [0,0,1,-1]
dt = [1,-1,0,0]
T = int(input())
for t in range(1,T+1):
    N=int(input())
    arr = [input() for _ in range(N)]
    for i in range(9):
        for char in arr[i]:
            if char == 'A':
                for k in range(4):
            elif char == 'B':
            elif char == 'C':