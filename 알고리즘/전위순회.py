def preorder(T):
    if T:
        print(T,end = ' ')
        preorder(left[T])
        preorder(right[T])

N=int(input())
E = N-1
arr = list(map(int,input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽번호 저장
right = [0]*(N+1)
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장
for i in range(E):
    p,c = arr[2*i],arr[2*i+1]
    if left[p]==0:
        left[p] =c
    else:
        right[p] =c
    par[c]=p
c=N
while par[c]!=0:        #부모가 있으면
    c=par[c]            #부모를 새로운 자식으로 두고
root = c
print(root)
preorder(root)