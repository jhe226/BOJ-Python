N, K = map(int, input().split())
coin_types = sorted([int(input()) for _ in range(N)], reverse = True)
cnt = 0

for coin in coin_types:
    cnt += K//coin
    K %= coin

print(cnt)