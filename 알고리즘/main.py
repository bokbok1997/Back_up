num =456789
c=[0]*12

for i in range(6):
    c[num%10]+=1
    num//=10

i=0
tri=run=0

while i<10:
    if c[i]>=3:
        c[i]-=3
        tri+=1
        print(c,tri)
        continue
    if c[i]>=1 and c[i+1]>=1 and c[i+2]>=1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run+=1
        print(c, run)
        continue
    i+=1
print(c,tri,run)