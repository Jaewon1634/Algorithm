"""
사고흐름
1) 직사각형이 1x1 크기의 정사각형으로 딱 구획이 나누어져 있다는 것 -> 결국 좌표 단위로 작동하는 구조를 만들어야겠다.
2) 최종 결과 출력 -> 안전 영역의 크기는 최종 영역에서 0 개수의 총합
3) 생각해야 할 조건들 정리
   - 기존 좌표가 바이러스로 인해서 변할 수 있는 조건
   - 안전 영역이 최대가 되도록 하기 위해서 벽 세 개를 어디에 세워야 할지(*)
   - 원소 탐색을 어떤 식으로 진행할 지
4) 한 번으로는 기존 좌표가 바이러스로 변하는지 구현 어려움 -> 반복을 통한 구현(만약 더이상 바이러스가 퍼지지 않는다면 break)
5) 어차피 행렬 자체 크기가 크지 않으니까 완전 탐색으로 벽 세우는 3개 좌표 모든 조합에 대해 해보고, 최대 안전영역을 갱신하는 느낌으로 해볼까(0에만 벽 세울 수 있으니)

** 해설 없이 손코딩한 raw 초안 **
from copy import deepcopy

# 기본 입력 
N, M = map(int, input().split())

# 초기 행렬 생성
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# 전체 좌표
coords = [(i, j) for i in range(N) for j in range(M)]
length = len(coords)

safe_area = 0

# 3중 반복문
for a in range(length):
    for b in range(a+1, length):
        for c in range(b+1, length):

            c1 = coords[a]
            c2 = coords[b]
            c3 = coords[c]

            # 초기 매트릭스 복사 
            matrix_copy = deepcopy(matrix)

            # 벽 세우기 (0일 때만 가능)
            can_build = True
            for x, y in [c1, c2, c3]:
                if matrix_copy[x][y] != 0:
                    can_build = False
                    break
            
            # 만약 세 개 좌표 중 하나라도 벽을 세울 수 없는 조합이면 건너띄기
            if not can_build:
                continue

            for x, y in [c1, c2, c3]:
                matrix_copy[x][y] = 1

            # 바이러스 확산
            while True:
                change = 0
                tmp = deepcopy(matrix_copy)

                # 상하좌우 검사
                for i in range(N):
                    for j in range(M):
                        if matrix_copy[i][j] == 0:
                            if i > 0 and matrix_copy[i-1][j] == 2:
                                tmp[i][j] = 2; change += 1
                            elif i < N-1 and matrix_copy[i+1][j] == 2:
                                tmp[i][j] = 2; change += 1
                            elif j > 0 and matrix_copy[i][j-1] == 2:
                                tmp[i][j] = 2; change += 1
                            elif j < M-1 and matrix_copy[i][j+1] == 2:
                                tmp[i][j] = 2; change += 1

                matrix_copy = tmp

                # 더 이상 퍼질 바이러스가 없으면 break
                if change == 0:
                    break

            # 안전 영역 계산
            count_safe_area = sum(row.count(0) for row in matrix_copy)

            if count_safe_area > safe_area:
                safe_area = count_safe_area

print(safe_area)

** 초안의 문제점 **
- 바이러스 확산 과정을 while + 전체 N×M 스캔으로 구현
- deepcopy를 통한 행렬 복사 시간복잡도가 높음
"""

# 수정안 - 덱 자료구조 사용
from collections import deque

# 입력
N, M = map(int, input().split())

# 리스트 컴프리헨션 사용 간단한 2차원 행렬화
matrix = [list(map(int, input().split())) for _ in range(N)]

# 전체 좌표
coords = [(i, j) for i in range(N) for j in range(M)]
length = len(coords)

# 최종 안전영역 크기
safe_area = 0

# 방향(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3중 반복문을 통한 좌표 조합은 그대로
for a in range(length):
    for b in range(a + 1, length):
        for c in range(b + 1, length):

            c1 = coords[a]
            c2 = coords[b]
            c3 = coords[c]

            # 벽 세울 수 없는 경우 반복 skip
            if matrix[c1[0]][c1[1]] != 0: continue
            if matrix[c2[0]][c2[1]] != 0: continue
            if matrix[c3[0]][c3[1]] != 0: continue

            # matrix 복사
            lab = [row[:] for row in matrix]

            # 벽 설치
            lab[c1[0]][c1[1]] = 1
            lab[c2[0]][c2[1]] = 1
            lab[c3[0]][c3[1]] = 1

            # 덱 구조를 사용한 바이러스 전파
            q = deque()

            # 2인 부분만 타겟해서 좌표 덱에 투입
            for i in range(N):
                for j in range(M):
                    if lab[i][j] == 2:
                        q.append((i, j))

            # 덱 모든 원소 빠져나올때까지, pop
            while q:
                x, y = q.popleft()

                # 상하좌우 원소 검사
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 만약 정사각형 안에 위치하고,
                    if 0 <= nx < N and 0 <= ny < M:
                        # 원소가 0이면 2로 바이러스 퍼지게 조정하고 
                        if lab[nx][ny] == 0:
                            lab[nx][ny] = 2
                            # 다시 덱에 투입
                            q.append((nx, ny))

            # 한 사이클 돌리면 최종 안전 영역 계산
            count = sum(row.count(0) for row in lab)
            
            # 기존 최대 안전 영역과 비교해서 새로운 벽 케이스가 더 안전 영역 크면 갱신 진행
            safe_area = max(safe_area, count)

print(safe_area)



