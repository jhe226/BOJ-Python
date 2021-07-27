A, B, C = map(int, input().split())
result = int(A/(C-B))
if B < C:
    print(f'{result + 1}')
else:
    print('-1')
