N = int(input())
P = list(map(int, input().split()))
P.sort()
time = 0
for i in range(N):
    for j in range(i+1):
        time += P[j]
    '''
    for i in range(N):
        time += P[i] * (N-i)
    '''

print(time)
