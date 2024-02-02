n = int(input())

if n % 4 == 0:
    result = n // 4
    s = result * 2
    print(s)
else:
    print(-1)