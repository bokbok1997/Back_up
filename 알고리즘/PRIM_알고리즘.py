import sys
sys.stdin = open('input1.txt','r')

# 우선순위 큐 활용을 위한 import
from heapq import heappush,heappop

def prim(start):
    pq = []             # 큐
    MST = [0] * V       # visited 느낌이다
    sum_weight = 0      # 최소 비용

    # 기존 bfs는 노드 번호만 관리
    # PRIM은 가중치가 낮으면 먼저 나와야 함
    # -> 관리해야 할 데이터 = 가중치,노드 번호
    # -> 동시에 두 데이터 다루기 => 1.클래스 만들기, 2.튜플
    heappush(pq,(0,start))  # pq에 시작점의 (가중치,노드번호) 추가 한다

    while pq:
        weight,now = heappop(pq)

        if MST[now]:            # BFS는 무조건 방문 하는데 Prim은 일단 큐에 넣고 방문
            continue            # 따라서 방문했다면 넘어가야 한다 (우선순위 큐의 특성!!!,BFS와 다른점)

        MST[now] = 1            # 방문 처리
        sum_weight+=weight      # 누적 합 추가

        for to in range(V):
            if graph[now][to] == 0 or MST[to]:      # 갈 수 없거나 이미 갔을때
                continue

            heappush(pq,(graph[now][to],to))
    print(f'최소 비용 : {sum_weight}')


V,E = map(int,input().split())
# 인접 행렬로 저장
graph = [[0]*V for _ in range(V)]
for i in range(E):
    s,e,w = map(int,input().split())
    graph[s][e] = w     # 가중치 만큼 저장
    graph[e][s] = w     # 무방향 그래프 이므로!
prim(0)