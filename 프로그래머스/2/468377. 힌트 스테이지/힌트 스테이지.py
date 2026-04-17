from itertools import product

# 완전 탐색
def solution(cost, hint):
    n = len(cost)
    min_cost = float('inf')
    
    for comb in product([0,1], repeat=n-1):
        hints_count=[0]*(n+1) # 힌트 번호, 힌트 카운트 인덱스 맞추기 위해서 n+1
        bundle_cost = 0 # 번들 비용
        
        for i in range(n-1):
            if comb[i]:
                bundle_cost += hint[i][0] # 조합 특정 번들 샀으면, 번들 비용
                for j in range(1, len(hint[i])): # 힌트 번호만
                    hints_count[hint[i][j]] += 1
                    
        total = bundle_cost
        
        # 스테이지별 총 비용 계산
        for stage in range(n):
            cnt = min(hints_count[stage+1], n-1)
            total += cost[stage][cnt]
        
        min_cost = min(min_cost, total)
                                    
    answer = min_cost
    return answer


# 입력 구성(cost, hint)
if __name__ == "__main__":
    n = int(input()) # cost 길이
    k = int(input()) # 한 번들 내 힌트권 개수
    cost_final = [] # 전체 cost 2차원 배열
    hint_bundle = [] # hint 번들 2차원 배열
    
    # cost 배열 구성
    for _ in range(n):
        cost_sub = [] # 임시 cost 1차원 배열
        for _ in range(n):
            a = int(input())
            cost_sub.append(a)
        cost_final.append(cost_sub)
    
    # hint 번들 배열 구성
    for _ in range(n-1):
        hint_sub = [] # 임시 hint 번들 1차원 배열
        price = int(input())
        hint_sub.append(price)
        for _ in range(k):
            hint_number = int(input())
            hint_sub.append(hint_number)
        hint_bundle.append(hint_sub)

    print(solution(cost_final, hint_bundle))
            