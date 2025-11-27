def digit(n):
    if n % 10 == 0:
        print('10')
    else:
        print(n % 10)

if __name__ == "__main__":
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        last_digit = pow(a, b, 10)
        digit(last_digit)
