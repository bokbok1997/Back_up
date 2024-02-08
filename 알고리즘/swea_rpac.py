# import sys
# sys.stdin = open("sample_in.txt", "r")
#

def func1(s, g):
    global top
    global stack
    if arr[s][g] == 1:
        return 1
    elif 1 in arr[s]:
        for i in range(1, V + 1):
            if arr[s][i] == 1:
                stack.append(i)
                top += 1
                return func1(i, g)
    elif stack:
        for i in range(1 + stack[top], V + 1):
            stack.pop()
            top -= 1
            return func1(i, g)
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
    s, g = map(int, input().split())
    stack = []
    top = -1
    print(f'#{tc} {func1(s, g)}')
