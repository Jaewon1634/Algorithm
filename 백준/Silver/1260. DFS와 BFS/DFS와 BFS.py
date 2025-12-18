"""
사고흐름
1) 입력 받는 그래프에 대한 정보를 DFS/BFS 활용할 수 있게끔 인접리스트로 재구성 해야겠다.
2) 각각 2차원 인접리스트로 표현된 그래프에 대해 DFS, BFS 각각 적용해서 출력한다.
"""
from collections import deque

# 노드 수, 간선 수, 시작 위치 초기값 입력
N, M, V = map(int, input().split())

# 그래프 2차원 인접 리스트로 초기화
graph = [[] for _ in range(N+1)]

# 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 각 노드 리스트 정렬
for i in graph:
    i.sort()

# dfs 함수 구성
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# bfs 함수 구성
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)