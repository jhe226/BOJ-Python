import sys

N, C = map(int, sys.stdin.readline().split())
h = [int(sys.stdin.readline()) for _ in range(N)]

def wifi_cnt(distance):
    cnt = 1
    cur_h = h[0]
    for i in range(1, N):
        if cur_h + distance <= h[i]:
            cnt += 1
            cur_h = h[i]
    return cnt

h = sorted(h)
start, end = 1, h[-1] - h[0]
result = 0

while start <= end:
    mid = (start + end)//2

    if wifi_cnt(mid) >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)