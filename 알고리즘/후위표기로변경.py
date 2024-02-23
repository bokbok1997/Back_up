icp ={'(': 3,'*':2,'/':2,'+':1,'-':1}
isp ={'(': 0,'*':2,'/':2,'+':1,'-':1}

stack = [0]*100
top = -1

fx = '(6+5*(2-8)/2)'
postfix = ''        #10보다 작은 수 만 들어온다고 가정하고 문자열로 넣자
for tk in fx:
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):  # 여는 괄호 push, top 원소보다 우선순위 높으면 push
        top+=1                # push
        stack[top] = tk
    elif (tk in '*/+-' and isp[stack[top]] >= icp[tk]):  # top 원소보다 우선순위 높지 않으면 pop
        while isp[stack[top]] >= icp[tk]:               # top 원소보다 우선순위가 낮을 때 까지 pop
            top-=1
            postfix += stack[top+1]
        top+=1
        stack[top] = tk                 # pop을 다 하고 자신을 push
    elif tk ==')':              # 닫는 괄호면, 여는 괄호를 만날 때 까지 pop
        while stack[top] != '(':
            top -= 1
            postfix += stack[top + 1]
        top -= 1        # 여는 괄호 pop 해서 버림
    else:
        postfix += tk
print(postfix)