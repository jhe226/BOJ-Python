T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    people = list(range(1, n+1))
    for j in range(k):
        for x in range(n-1, 0, -1):
            people[x] = sum(people[:x+1])
    print(people[-1])
