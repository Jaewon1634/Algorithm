n, m = map(int, input().split())
board = [input() for i in range(n)]

white_start = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    ]

black_start = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

change = []

for i in range(n-7):
    for j in range(m-7):
        black_change = 0
        white_change = 0

        for r in range(8):
            for c in range(8):
                if board[i+r][j+c] != black_start[r][c]:
                    black_change +=1
                if board[i+r][j+c] != white_start[r][c]:
                    white_change +=1
        change.append(min(black_change, white_change))

print(min(change))  