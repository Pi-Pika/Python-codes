t = int(input())

for i in range(0, t):
    n = int(input())
    a_list = list(map(int, input().split()))
    s = sum(a_list)
    b = int(s/n)
    c = 0
    c3 = 0
    if n == 1:
        print("YES")
    else:
        for j in a_list:
            if j >= b:
                c += j-b
            else:
                c1 = b-j
                if c >= c1:
                    c -= c1
                else:
                    c3 = 1
                    break
        if c3 == 1:
            print("NO")
        else:
            print("YES")
