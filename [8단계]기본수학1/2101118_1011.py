import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    d = y - x - 1
    n = int(math.sqrt(d))

    if y-x > n*n + n:
        print(2*n+1)
    else:
        print(2*n)





