import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
card_num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_num = list(map(int, sys.stdin.readline().split()))

card_num.sort()

for a in M_num:
    right_index = bisect_right(card_num, a)
    left_index = bisect_left(card_num, a)
    print(right_index - left_index, end=' ')