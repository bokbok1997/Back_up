N = int(input())
M = int(input())
S = input()
cnt = 0
data = ''
for i in S:
    if i=='O': data+='0'
    else: data+='1'
filter = int('10'*N+'1',2)
res = int('11'*N+'1',2)
lll=(len(data))
data=int(data,2)
for i in range(lll-2*N+1):
    if data & (res<<i) == (filter<<i):
        cnt+=1
print(cnt)