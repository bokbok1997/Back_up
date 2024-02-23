# 최대 힙
def enq(n):
    global last
    last += 1       # 마지막 노드 추가 (완전 이진 트리 유지)
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # 부모 > 자식 비교를 위해
    p = c // 2      # 부모 번호 계산
    while p>=1 and h[p]>h[c]:
        h[p],h[c] = h[c],h[p]
        c = p
        p = c //2

def deq():
    global last
    tmp = h[1]
    h[1] = h[last]
    last-=1
    p = 1
    c=p*2
    while c<=last:          # 자식이 있으면
        if c+1<=last and h[c] < h[c+1]:     # 만약 오른쪽이 더 크면
            c+=1
        if h[p]<h[c]:
            h[p],h[c]=h[c],h[p]
            p=c
            c=p*2
        else:
            break
    return tmp

N = 10              # 필요 노드 수
h = [0]*(1+N)       # 최대 힙
last = 0            # 힙의 마지막 노드 번호 = 0
for i in [2,5,3,6,4]:
    enq(i)
    print(h)
while(last>0):
    print(deq())