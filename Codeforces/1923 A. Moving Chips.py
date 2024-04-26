t = int(input())

for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))

    x = a.index(1)
    y = len(a) - 1 - a[::-1].index(1)
    c = a[x:y + 1].count(0)
    print(c)
