"""
사고흐름
1) 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구해야 하므로 그리디
2) 그리디가 될 수 있는 이유, 근거 - 누적 구조이기 때문에 앞 순서가 빠르게 돈을 뽑을 수록 좋음
3) 구현
"""
N = int(input())
array = list(map(int, input().split()))

array.sort()

sum = 0

# 누적 구조 설계
for i in range(len(array)):
    for j in range(i+1):
        sum += array[j]
        
print(sum)