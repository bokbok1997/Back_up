import sys
sys.stdin = open("input.txt", "r")

T= int(input())
for tc in range(1, T + 1):
    N,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]