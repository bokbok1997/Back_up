def Brute_Force(p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        print(t[i], p[j])
        if t[i] != p[j]:
            i = i-j
            j=-1
        i = i+1
        j = j+1
    if j == M: return i-M       # 검색 성공
    else: return -1             # 검색 실패

def fff(p,t):
    for i in range(N-M+1):      # text에서 비교 시작 위치
        for j in range(M):
            if t[i+j] != p[j]:  # 불일치 하면 다음 시작위치로
                break
        else:                   # 패턴 매칭 성공하면
            return 1
    return 0                    # 모든 위치 비교가 끝난 경우

p = "is"  # 찾을 패턴
t = "This is a book~!"  # 전체 택스트
M = len(p)  # 찾을 패턴 길이
N = len(t)  # 전체 택스트 길이

print(Brute_Force(p,t))
print(fff(p,t))