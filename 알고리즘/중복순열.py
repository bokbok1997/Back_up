def fff(x,t):                 # 중복순열
    if x == N:              # Level => x는 0부터 4까지 5번 거쳐간다
        print(*path)        # 마지막 레벨에서 출력
        return
    if t==1:            #타입 1은 중복순열
        for i in range(1,B):   # Branch가 1~4,(가지 몇개?)
            path.append(i)
            fff(x+1,1)
            path.pop()
    else:               # 타입 2는 순열
        for i in range(1, B):  # Branch가 1~4,(가지 몇개?)
            if used[i] == True:  # used가 1 이면
                continue
            used[i] = True  # 방문기록 추가
            path.append(i)
            fff(x + 1,2)
            path.pop()
            used[i] = False  # 방문기록 삭제

path = []
N = 2
B = 7
used = [False]*B             # Branch 크기와 같이 초기화
fff(0,2)