import sys

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
N.sort()
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    print(binary_search(N, M[i], 0, n-1))