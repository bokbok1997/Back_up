# 이진 검색이므로 삽입하는 배열이 오름차순으로 정렬 되어 있어야 한다
def binary_search(arr, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == key:      # 검색 성공
            return middle
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1
print(binary_search([1,2,3,5,6,10,12,19,22,36,66,110,112],13,66))