tc = int(input())
i = 0
while 1:
    if i == tc:
        break
    a = int(input())
    b = input()

    for x in range(a):
        if b[x] == "B":
            m = x
            int(m)
            break

    for x in reversed(range(a)):
        if b[x] == "B":
            t = x
            break
    i += 1
    print(t-m+1)
