import sys
sys.stdin=open('input1.txt','r')

def merge(left,right):
    global cnt
    if left[-1] > right[-1]: cnt += 1
    result=[0]*(len(left)+len(right))
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result[i+j]=left[i]
            i+=1
        else:
            result[i+j]=right[j]
            j+=1
    while i<len(left):      # left의 원소만 남은 경우
        result[i+j]=left[i]
        i += 1
    while j < len(right):  # right의 원소만 남은 경우
        result[i + j] = right[j]
        j += 1
    return result

def msort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2

    left =arr[:mid]
    right=arr[mid:]

    left = msort(left)      # 왼쪽 절반 분할
    right = msort(right)    # 오른쪽 절반 분할할

    return merge(left,right)



T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    data = list(map(int,input().split()))
    data = msort(data)
    print(f'#{tc+1} {data[N//2]} {cnt}')
