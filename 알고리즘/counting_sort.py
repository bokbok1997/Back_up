N=6
K=9
data = [7,2,4,5,1,3]  # 조건 0~9
counts=[0]*(K+1)
temp =[0]*(K+1)       # 정렬된 결과 저장용
# counts 배열에 기록하기
for x in data:
    counts[x] +=1
print(f'N={N}, K={K}\n배열 : {data}')
print(f'개수 : {counts}')
# counts 누적합 만들기
for i in range(1,K+1):
    counts[i]=counts[i]+counts[i-1]
print(f'누적 : {counts}')
# data 마지막 원소부터 정렬하기
for i in range(N-1,-1,-1):
    counts[data[i]] -= 1   # 개수를 인덱스로 변환
    temp[counts[data[i]]] = data[i]
print(f'정렬 : {temp}')
