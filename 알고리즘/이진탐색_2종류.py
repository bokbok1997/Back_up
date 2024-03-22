# 이진검색 O(log(n))
arr = [3,12,23,44,7,2,4,8]

# 1. 정렬된 상태의 데이터
arr.sort()

# 2. 이진 검색 반복문 버전
def bin_search(target):
    cnt = 0
    low = 0
    high = len(arr) - 1

    # 해당 숫자 찾으면 종료 or 더 이상 찾을 수 없을 때 까지 반복
    while low<=high:
        mid = (low+high)//2
        cnt+=1

        if arr[mid]==target:
            return mid,cnt
        elif arr[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1,cnt
print(arr)
print(f'23의 인덱스 = {bin_search(23)}')

# 3. 재귀함수 버전
def bin_2(target,low,high):
    if low>high:
        return -1
    else:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return bin_2(target,low,mid-1)
        else:
            return bin_2(target,mid+1,high)
print(arr)
print(f'23의 인덱스 = {bin_2(23,0,len(arr)-1)}')