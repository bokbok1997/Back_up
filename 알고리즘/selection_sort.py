def selection_sort(arr,n):   # 오름차순으로 정렬
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)
    return 0

def select(arr,k):      # k개의 개수까지만 오름차순으로 정렬
    for i in range(0,k):        # k번 까지만 정렬
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr[:k])
    return 0




aaa=[10,9,5,1,5,0,-2,15,33,70,6,4]
selection_sort(aaa,len(aaa))
select(aaa,6)