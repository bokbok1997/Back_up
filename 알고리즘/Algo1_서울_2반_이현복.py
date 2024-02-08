di = [0,1,0,-1]     # 델타를 이용
dj = [1,0,-1,0]
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    max_score = 0          # 최대 값을 이용해야 하므로 비교하기 위한 변수 초기하
    for i in range(N):
        for j in range(N):
            temp_score = 0          # 각 칸을 순회하면서 사용할 점수를 저장 할 변수 최기화
            for path in range(4):   # 델타를 이용하기 위해 range로 상하 좌우를 모두 근접
                if 0<=i+di[path]<=N-1 and 0<=j+dj[path]<=N-1:  # 상하좌우의 위치가 존재하는 칸 일때만
                    temp_score += data[i+di[path]][j+dj[path]]  # 점수에 상하좌우 값을 더해준다
            temp_score -= data[i][j]            # 점수에 맞은 칸의 점수를 빼준다
            if i == 0 or i == N-1 or j == 0 or j ==N-1:   # 가장자리에 맞은 경우
                temp_score = 0
            elif temp_score < 0:                          # 점수 합산 결과가 음수인 경우
                temp_score = 0
            elif temp_score % 2 == 0:                     # 점수 합산 결과가 양수인 경우
                temp_score *= 2
            if max_score <= temp_score:   # 기존의 최대값 보다 크면 값 갱신
                max_score = temp_score
    print(f'#{tc} {max_score}')
