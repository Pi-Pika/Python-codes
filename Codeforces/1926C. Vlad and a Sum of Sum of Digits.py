t = int(input())

for i in range(0, t):
    n = int(input())
    ans = 0

    a = n//9
    ans += a*45

    b = n%9
    k = 1
    for j in range(0, b):
        ans += k
        k += 1
    print(ans)

