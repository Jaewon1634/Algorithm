"""
사고흐름
1)정점 개수와, 간선 정보 주어져있으니 인접 리스트를 통한 그래프 표현 구성
2)1번과 건너건너 연결되어 있는 모든 정점까지 탐색 한 후 노드 수를 구하면 되는 문제이므로, DFS/BFS 어떤 것을 사용해도 좋을 것 같은데?  
"""

# 노드 수 입력 
M = int(input())

# 간선 수 입력
N = int(input())

# 인접 리스트 구성
graph = [[] for _ in range(M+1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# virus_dfs 구성, stack을 통해 구현
visited = [False] * (M+1)

def virus(graph, v, visited):
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            virus(graph, i, visited)
    return visited
            
# 시작 1번 지점은 빼야 하므로 cnt
cnt = 0
for i in virus(graph, 1, visited):
    if i:
        cnt += 1

print(cnt-1)
    