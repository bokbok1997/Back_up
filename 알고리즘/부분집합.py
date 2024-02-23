def f(i,k,s,t):       # k개의 원소를 가진 배열A, 부분집합의 합이  t인 경우
    if s == t:
        for j in range(k):
            if bit[j] :
                stack.append(A[j])
                # print(A[j], end=' ')
        # if len(stack) == t:
        #     print('sdds')
        print(stack)
        print()
    elif i == k:    # 부분집합 출력
        return
    elif s>t:
        return
    else:
        for j in range(1,-1,-1):
            bit[i] = j
            f(1 + i, k, s + A[i]*j, t)

A =[1,2,3,4,5,6,7,8,9,10,11,12]
N=3
bit = [0]*N         # bit[i]는 A[i]가 부분집합에 포함되는지 표시
cnt=0
stack = []
f(0,N,0,K)
print('cnt : ',cnt)