arr=['A','B','C','D','E']
n = 5

def get_sub(tar):
    cnt = 0
    for i in range(n):
        if tar& 0x1:        # LSB 가 1인지 확인
            cnt+=1
            # print(arr[i],end=' ')
        tar >>=1        # right shift 비트연산 -> 오른쪽 끝 비트제거
    return cnt
res = 0
for tar in range(1<<n):
    if get_sub(tar)==3:
        res+=1
print(res)

# for i in range(1<<5):
#     print(bin(i))