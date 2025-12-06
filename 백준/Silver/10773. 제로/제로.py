"""
사고흐름
1) 수를 리스트에 넣고 0이 나오면 가장 최근 것을 지우는 것 -> 리스트를 활용하여 0이면 가장 마지막 원소를 삭제
"""

K = int(input())
money = []

for _ in range(K):
    a = int(input())
    if a != 0:
        money.append(a)
    else :
        money.pop()

print(sum(money))