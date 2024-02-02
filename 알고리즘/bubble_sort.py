def bubble_sort(list,n):
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[1 + j]:
                arr[j], arr[1 + j] = arr[1 + j], arr[j]
    return 0

N =6
arr = [7,2,5,3,1,4]
bubble_sort(arr,N)
print(arr)