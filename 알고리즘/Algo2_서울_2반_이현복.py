T = int(input())
for tc in range(1,1+T):
    N,K = map(int,input().split())
    data = list(map(int,input().split()))
    index,sum =0, 0        # 개구리의 위치를 받아올 변수 index 와 밟은 연잎의 숫자 합을 저장할 sum변수
    back = 0               # 음수가 나온뒤 양수가 나왔을 때 뒤로간 만큼 앞으로 가기위해 사용 할 변수
    for jump in range(K):
        if index < 0 or index > N-1:  # 주어진 범위를 벗어나면 더이상 점프를 하지 않는다
            break
        elif jump == 0:               # 첫 점프
            index += data[index]
        elif data[index] <= 0:        # 음수인 연잎을 밟았을때
            back = (-1) * data[index]
            sum += data[index]
            index += data[index]
        elif data[index] > 0 and back != 0:     # 뒤로 갔다가 닷 앞으로 가는 경우
            sum += data[index]
            index += (back + data[index])
            back = 0
        elif data[index] > 0:                   # 양수인 연잎을 밟았을때
            index += data[index]
            sum += data[index]

        if jump == K-1:                         # 주어진 횟수만큼 탈출하지 않고 순회 할 경우
            sum += data[index]                  # 마지막에 밟은 연잎의 값을 더해준다
    print(f'#{tc} {sum}')
