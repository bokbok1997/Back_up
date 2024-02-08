aaa='(()))'
stack=[0]*10
top=-1
for i in aaa:
    if i == '(':
        top+=1
        stack[top]=i
    elif i ==')':
        if top > -1:
            top-=1
        else:
            print('Under_Flow')
print(stack,top)