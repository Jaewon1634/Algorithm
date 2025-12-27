N = int(input())

num = []

for i in range(N):
    a = int(input())
    num.append(a)
    
num.sort()

for j in num:
    print(j)