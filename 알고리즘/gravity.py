N = int(input())
arr=list(map(int, input().split()))
result=[]
max_v=0
for i in range(N-1):
    cnt = 0
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            cnt +=1
    if max_v < cnt:
        max_v = cnt
print(max_v)