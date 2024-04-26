t = int(input())

for i in range(0, t):
    n = int(input())
    c = 0
    count = 0

    for j in range(0, n):
        a = input()
        a1 = a.count('1')

        if (a1 > c or a1 < c) and a1 != 0:
            c = a1
            count += 1

    if count > 1:
        print("TRIANGLE")
    else:
        print("SQUARE")
