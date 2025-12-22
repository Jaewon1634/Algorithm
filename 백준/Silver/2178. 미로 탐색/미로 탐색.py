"""
사고흐름
1) 입력은 우선 리스트 형태의 2차원 배열로 받아야 겠다.
2) 각 칸이 노드이고, 1로 표현된 이동할 수 있는 모든 노드 사이는 간선으로 연결되어 있다.
3) 어떤 그래프 탐색 알고리즘을 적용해야 할 까? -> BFS/DFS
4) DFS는 일단 시작점에서 한 경로를 끝날 때 까지 길게 탐색하는 것이기 때문에, 직선거리로 가던, 돌아가던 최단 경로를 보장할 수 없다.
5) 그렇다면 BFS는 한번 이동, 두번 이동, 세번 이동을 단계적으로 탐색하기 때문에 거리를 최소로 하면서 탐색하는 것에는 무조건 DFS보다 BFS가 유리하다.
6) DFS는 덱 불러와서 큐로 구현하고, 방문 처리 할 리스트 만들어야 하고, 이전 배열 문제 풀었을 때 처럼 이동은 dx, dy로 해서 좌표 형태로 갱신해나가야겠다.
7) 최소 거리 자체는? -> 각 좌표 방문 거리 리스트 따로 만들어서 계산
"""
# 덱 자료구조 라이브러리
from collections import deque

# 격자 크기 입력 받기
N, M = map(int, input().split())

# 그래프 구성
graph = [list(map(int, input())) for _ in range(N)]

# 이동 표현(상,하,좌,우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# BFS 알고리즘 구성(시작 지점 파라미터)
def bfs(x, y):
    queue = deque()
    queue.append((x,y)) # 초기 좌표 큐에 입력
    
    # 좌표 수 만큼 방문 여부 리스트 구성
    visited = [[False] * M for _ in range(N)]
    
    # 좌표 수 만큼 방문 거리 리스트 구성
    distance = [[0] * M for _ in range(N)]
    
    # 초기 지점 방문 처리 및 거리 갱신
    visited[x][y] = True
    distance[x][y] = 1
    
    # 더 이상 큐에 넣을 새로운 탐색 노드 후보가 없을 때 까지
    while queue:
        x, y = queue.popleft()
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 격자 내부 범위 검사
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
        
            # 이동 가능이고, 아직 방문하지 않은 노드라면
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True # 먼저 방문처리
                distance[nx][ny] = distance[x][y] + 1 # 무조건 방문 비용 1이라, 이전 노드 거리 값보다 1 추가해가면서 갱신
                queue.append((nx, ny)) # 큐에 추가
        
    return distance[N-1][M-1] # 맨 마지막 리스트 인덱스 거리 출력

print(bfs(0, 0))
