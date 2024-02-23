def change_num(n,a):            # n은 바꾸기를 원하는 십진수, a는 바꾸고자 하는 진수(16이하)
    if n<a:                     # 마지막 상황
        if 9<n<16:              # 11~16진수일때
            n = num_alpha[str(n)]    # 알파벳으로 대체
        return str(n)
    else:
        tmp = change_num(n // a, a)
        res = str(n%a)          # 나눈 나머지
        if 9<n%a<16:            # 11~16진수일때
            res = num_alpha[str(n%a)]
        return tmp+res

def backtoten(n,a):             # a진수로 표현된 숫자 n을 10진수로
    res = 0
    tmp = str(n)
    length = len(tmp)
    for i in tmp:
        length-=1
        res+=int(i)*a**length   # i 곱하기 a의 length승을 계산해서 res에 더한다
    return res

def change_2_16(b):             # 2진수를 16진수로
    b=str(b)
    stack=[]
    top = 0
    for i in b:
        stack.append(i)
    res = ''
    while top<len(stack):
        a=b=c=d='0'
        try:
            a = stack.pop()
            b = stack.pop()
            c = stack.pop()
            d = stack.pop()
        except:
            pass
        res=(change_num(backtoten(int(d+c+b+a), 2),16))+res
    return res

def change_16_2(x):
    res11=''
    for i in str(x):
        res=change_num(backtoten(x,16),2)+res
    return res11


num_alpha ={
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}
# sss = change_num(75,2)
# ssss = change_num(75,16)
# print(sss,ssss)
print(backtoten(10011,2))
# print(change_2_16(sss))
# print(change_16_2(ssss))