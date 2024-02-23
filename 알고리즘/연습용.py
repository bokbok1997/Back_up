# import sys
# sys.stdin = open("sample_input.txt", "r")

password={
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9,
}
T = int(input())
for tc in range(T):
    N,M=map(int,input().split())
    data=[('1'+input()) for _ in range(N)]
    for i in data:
        arr =str(bin(int(i,16)))[3:]
        lll = len(arr)
        # print(arr)
        for i in range(lll):
            wonbin = [0, 0, 0, 0]
            if arr[lll-1-i] == '1':
                test = arr[lll-i-7:lll-i]
                comp = test[0]
                a= 0
                cnt=1
                for j in test[1:]:
                    if comp!=j:
                        wonbin[a]+=cnt
                        cnt=0
                        a+=1
                        comp = j
                    cnt += 1
                else: wonbin[a]+=cnt
                res=''
                for aa in wonbin:
                    res+=str(aa)
                try:
                    password[res]
                except:
                    break
                break


