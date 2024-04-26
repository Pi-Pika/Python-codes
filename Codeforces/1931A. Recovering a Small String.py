t = int(input())
for i in range(0, t):
    n = int(input())
    c = 0
    for j in range(1, 27):
        for k in range(1, 27):
            for l in range(1, 27):
                if (j + k + l) == n:
                    print(chr(j+96)+chr(k+96)+chr(l+96))
                    c = 1
                    break
            if c == 1:
                break
        if c == 1:
            break
