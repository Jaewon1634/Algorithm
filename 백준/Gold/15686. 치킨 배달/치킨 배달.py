"""
사고흐름
1) 치킨집 조합을 먼저 고르고, 그 조합에 대해 모든 집의 최소 거리 합을 계산, 최솟값 갱신
2) 못한 점 : 조합에 대한 표현? (-> combinations 활용)
"""

import sys
from itertools import combinations

N, M = map(int, input().split())

houses = []
chickens = []

# 좌표 분리
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chickens.append((r, c))

# 집, 치킨 거리 미리 계산
dist = [[0] * len(chickens) for _ in range(len(houses))]

for i, (hr, hc) in enumerate(houses):
    for j, (cr, cc) in enumerate(chickens):
        dist[i][j] = abs(hr - cr) + abs(hc - cc)

# 치킨집 조합 탐색
answer = float('inf')

for comb in combinations(range(len(chickens)), M):
    total = 0

    # 집 기준 최소 거리 합
    for i in range(len(houses)):
        total += min(dist[i][j] for j in comb)

        # 이미 최소 이상 이면 굳이 갱신 안해도
        if total >= answer:
            break

    answer = min(answer, total)

print(answer)
