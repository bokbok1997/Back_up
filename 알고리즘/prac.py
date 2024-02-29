import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(T):
    line = input()
    lll = len(line)
    cnt = 0
    res = 0
    for i in range(lll):
        if line[i]=='(':
            cnt+=1
        elif line[i]==')' and  line[i-1]=='(':
            cnt-=1
            res+=cnt
        else:
            res += 1
            cnt -= 1
    print(res)