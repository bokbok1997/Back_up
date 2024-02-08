def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def f(i,k):     # i는 현재위치, k는 목표
    if i == k:
        print(brr)
        return
    else:
        # print(arr[i])
        brr[i]=arr[i]
        f(i+1,k)

arr=[10,20,30]
N = len(arr)
brr=[0]*N
f(0,N)

# for i in range(10):
#     print(fibo(i),end=' ')