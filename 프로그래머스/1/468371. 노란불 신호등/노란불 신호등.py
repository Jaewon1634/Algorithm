import math
from functools import reduce

# 초,노,빨 순서가 같기 때문 각 신호등 주기의 최소공배수까지가 한 사이클, 그 이후로 동일

# 두 수의 최소공배수
def lcm(a,b):
    return abs(a*b) // math.gcd(a,b)

# 여러 수의 최소공배수는 reduce로 반복 적용
def lcm_list(numbers):
    return reduce(lcm, numbers)

def solution(signals):
    answer = 0
    
    period = [(g+y+r) for g,y,r in signals]
    min_period = lcm_list(period)
    
    for t in range(1, min_period+1):
        all_yellow = True
        
        # 신호등 하나씩 탐색
        for g,y,r in signals:
            period = g+y+r
            
            # 노란불도 지속시간이 있기 때문에, 나머지 활용
            mod = t % period
            
            # 하나라도 노란불이 아니라면 pass하고 다음 시간
            if not(g+1<=mod<=g+y):
                all_yellow = False
                break
            
        # 만약 모두 노란불이면 그대로 시각 출력
        if all_yellow:
            return t
    
    # 최소공배수 주기 다 돌았는데 없으면 -1 출력
    return -1