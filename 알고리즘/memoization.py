# memo를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로, memo[1]는 1로 초기화
def fibo_memo(n):
    global cnt
    cnt+=1
    if n!=0 and memo[n]==0:
        memo[n]= fibo_memo(n-1)+fibo_memo(n-2)
    return memo[n]
def fibo(n):
    global cnt2
    cnt2+=1
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


cnt = 0
cnt2=0
n=7
memo = [0]*(n+1)
memo[0]=0
memo[1]=1
print(fibo_memo(n),cnt)
print(fibo(7),cnt2)
print(memo)