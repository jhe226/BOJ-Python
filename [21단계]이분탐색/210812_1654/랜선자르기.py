K, N = map(int,input().split())

l = []
for i in range(K):
    l.append(int(input()))

start = 1
end = max(l)

while True:
    if start > end:
        break
    cnt = 0
    mid = (start+end) // 2
    for n in l:
        cnt += n // mid
    if cnt >= N:
        start = mid + 1
    else :
        end = mid - 1

print(end)
