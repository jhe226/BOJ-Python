n = int(input())
cnt = 0
up = 0
end = 0
while n > end:
    up += 1
    cnt += 1
    end += up
a = end - n + 1
b = cnt + 1 - a
if cnt % 2 == 0:
    print('{}/{}'.format(b, a))
else:
    print('{}/{}'.format(a, b))