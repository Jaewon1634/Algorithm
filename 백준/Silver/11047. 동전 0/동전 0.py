"""
사고 흐름
1)K원을 배수 관계의 동전 단위로 만드는 문제인데, 최소 개수로 달성해야 하므로 그리디로 접근 가능
2)배수 관계이기 때문에, 이 때는 무조건 큰 단위부터 사용하면 되므로 간단한 문제
"""

N, K = map(int, input().split())

coin = []

for _ in range(N):
    M = int(input())
    coin.append(M)

coin.sort(reverse=True)

count = 0

for c in coin:
    if K == 0:
        break
    count += K // c       
    K %= c                

print(count)
        