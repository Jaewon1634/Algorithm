"""
사고 흐름
1) 최소를 구하라고 했으니 경우에 따라서 그리디로 풀어도 되지 않을까..?
2) 수식에 +,- 밖에 없으니 최소의 경우 +는 영향력이 없고 무조건 -의 영향력을 키우는 방향으로 그리디하게 가면 되겠네..?
3) 괄호를 어떻게 표현하지? 굳이 괄호가 필요한가?
4) 일단 입력을 받고, 리스트로 부호 살려서 그대로 수만 추출 ex) 100+15-40+90-30 -> [100, 15, -40, 90, -30]
5) -가 나올때 까지는 부호 그대로, -가 나온 후 그 다음 -가 나올 때 까지 사이에 끼어있는 +만 부호 반전, 괄호 역할 -> [100, 15, -40, -90, -30]
"""

expr = input()

result = []
current = ""

# 중간지점 두어서 +나올때 까지 숫자 저장하고 비우고 반복
for i in expr:
    if i in "+-":
        if current:
            result.append(int(current)) #일단 기존 값 result에 채우고,
        current = i #현재 값을 부호로 대치하여 다시 누적 시작
    else:
        current += i

result.append(int(current))  # 마지막 값 추가

# 리스트 기반으로 부호 바꾸는 룰 적용하여 수식 계산
minus = False

for i in range(len(result)):
    if result[i] < 0:
        minus = True
    elif minus:
        result[i] = -result[i] # 인덱스 기반으로 값 부호 변경

print(sum(result))
