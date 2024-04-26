t = int(input())

for j in range(0, t):
    n, s = [int(a) for a in input().split()]
    ch = "a"
    for i in range(0, n):
        for k in range(0, s):
            print(ch, end="")
        ch = int(ch)
        ch += 1
        ch = str(ch)
        ch = "a"
    print()
