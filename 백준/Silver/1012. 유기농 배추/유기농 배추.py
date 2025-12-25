"""
사고흐름
1) 단지 개수를 맞추는 문제와 거의 동일한 메커니즘으로, 가능할 때 까지 탐색 반복
"""

from collections import deque

def bfs(sr, sc, graph, visited, N, M):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True
    
    # 4방향 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]
            
            # 범위 검사
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    return 1


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    # 그래프 초기화
    graph = [[0] * M for _ in range(N)]
    
    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1 
    
    visited = [[False] * M for _ in range(N)]
    
    count = 0
    
    # 군집 개수 탐색
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 1 and not visited[r][c]:
                count += bfs(r, c, graph, visited, N, M)
    
    print(count)

        