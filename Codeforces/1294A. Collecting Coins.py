t = int(input())

for i in range(0, t):
    s = 0
    a, b, c, n = [int(x) for x in input().split()]
    s += a+b+c+n
    if s % 3 != 0 or s/3 < a or s/3 < b or s/3 < c:
        print("NO")
    else:
        print("YES")
