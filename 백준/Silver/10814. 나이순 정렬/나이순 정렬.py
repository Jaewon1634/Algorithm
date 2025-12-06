"""
사고 흐름
1) 나이가 우선순위, 후순위가 가입한 순번
2) 리스트를 중심으로 뭔가 정렬을 계속 해나가야 겠다. -> 리스트가 비어있으면 그냥 넣기
3) 리스트가 차있다면, 나보다 큰 숫자가 들어오기 전까지 계속 인덱스 오른쪽으로 넘기다가 큰 숫자 들어오면 그 위치에 삽입
"""

"""
초기 답변
N = int(input())
answer = []

for _ in range(N):
    number, name = input().split()
    number = int(number)

    if len(answer) == 0:
        answer.append((number, name))
    else:
        index = 0
        for i in range(len(answer)):
            if number >= answer[i][0]:
                index += 1
            else:
                break
        answer.insert(index, (number, name))

for a, b in answer:
    print(a, b)
    
** 시간초과 -> 삽입 정렬은 시간 복잡도 높음
"""

"""
수정 사고흐름
1) 리스트 sort는 키를 지정할 수 있음, 순서에 해당하는 인덱스를 입력받아 key에 추가
"""
# 수정 답변
N = int(input())
answer = []

for idx in range(N):
    number, name = input().split()
    answer.append((int(number), idx, name))

# 나이 → 입력 순서 기준 정렬
answer.sort(key=lambda x: (x[0], x[1]))

for age, _, name in answer:
    print(age, name)

