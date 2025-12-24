"""
사고흐름
1) 이동을 해가면서 탐색을 진행해야 하니, dx와dy는 반드시 사용할 것 같다.
2) 순차적으로 우상단부터 1 발견하면 탐색하고 단지와 단지 수 저장 해놓고 출력
"""
# 탐색을 위한 deque 구조
from collections import deque

# 그래프 크기 입력
N = int(input())

# 그래프 구성
graph = [list(map(int, input())) for _ in range(N)]

# 이동 표현
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 방문
visited = [[False] * N for _ in range(N)]

# BFS 알고리즘 구성
def bfs(x, y):
    queue = deque()
    queue.append((x,y)) # 초기 좌표 큐에 입력
    
    # 초기 지점 방문 처리 및 거리 갱신
    visited[x][y] = True
    count = 1
    
    # 더 이상 큐에 넣을 새로운 탐색 노드 후보가 없을 때 까지
    while queue:
        x, y = queue.popleft()
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 격자 내부 범위 검사
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
        
            # 이동 가능이고, 아직 방문하지 않은 노드라면
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True # 먼저 방문처리
                queue.append((nx, ny)) # 큐에 추가
                count += 1
        
    return count

# 단지 수
house = []

for i, j in enumerate(graph):
    for k, l in enumerate(j):
        if l == 1 and not visited[i][k]:
            house.append(bfs(i,k))
            
house.sort()

print(len(house))
for m in house:
    print(m)

    

