import sys
N = int(sys.stdin.readline())
meeting_time = []
for _ in range(N):
    H, M = map(int, input().split())
    meeting_time.append((H, M))
meeting_time = sorted(meeting_time, key = lambda x:x[0])
meeting_time = sorted(meeting_time, key = lambda x:x[1])

cnt = 0
time = 0

for x in meeting_time:
    if x[0] >= time:
        time = x[1]
        cnt += 1

print(cnt)