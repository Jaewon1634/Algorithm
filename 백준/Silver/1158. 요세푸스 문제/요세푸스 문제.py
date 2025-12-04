"""
사고흐름
1)문제에 대한 이해 -> 1번부터 N번까지 사람들이 원형으로 앉아 있고, K번째 사람을 제거하고, 제거된 사람 다음 사람부터 다시 K번째 사람을 세어서 제거 -> 사람이 다 없어질 때까지 반복
2)어떤 식으로 구현할까? -> 인덱스도 활용해야 될 것 같고, 중간 변수를 두어야 할 것 같기도 하다.
3)리스트를 기본으로 하고, 값 자체, 제거 해야할 인덱스를 중심으로 구현
"""

N, K = map(int, input().split())

original_list = [i for i in range(1, N+1)]
answer_list = []

turn = 1
index = K-1
length = len(original_list)

while turn <= N :
    value = original_list.pop(index)
    length -= 1
    if length != 0 :
        index = (index+K-1) % length
    else:
        pass
    answer_list.append(str(value))
    turn +=1
        
print(str('<') + ", ".join(answer_list) + str('>'))