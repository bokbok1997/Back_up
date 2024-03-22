'''
1. 전체 그래프를 보고, 가중치를 제일 작은 간선 부터 뽑자
    -> 코드로 구현 : 전체 간선 정보 저장 + 가중치로 정렬

2. 방문 처리
    -> 이 때, 사이클이 발생하면 안된다.!
    -> 사이클 여부??? => union-find 알고리즘 활용
'''

import sys
sys.stdin = open('input1.txt','r')

def find_set(x):
    if x == parents[x]:
        return x
    # 경로 압축
    parents[x]=find_set(parents[x])
    return parents[x]

def union(a,b):
    a=find_set(a)
    b=find_set(b)
    # 같은 집합이면 pass
    if a==b:
        return
    if a<b:
        parents[b]=a
    else:
        parents[a] = b
    parents[find_set(b)] = find_set(a)

V,E = map(int,input().split())
edges = []  # 간선 정보들을 모두 저장
for _ in range(E):
    s,e,w = map(int,input().split())
    edges.append([s,e,w])
edges.sort(key=lambda x:x[2])   # 가중치를 기준 으로 정렬
parents = [i for i in range(V)]

# MST완성은
cnt = 0
sum_weight = 0

for s,e,w in edges:         # 간선을 모두 확인
    # 싸이클이 발생하면 pass
    #   -> 이미 같은 집합에 속해 있다면(=대표자가 같다면) pass
    if find_set(s) == find_set(e):
        continue
    cnt+=1
    # 싸이클이 발생하지 않으면 방문 처리
    union(s,e)
    sum_weight+=w

    if cnt == V-1: # MST완성!!, 간선의 개수 ==ㅍ-1
        break
print(sum_weight)