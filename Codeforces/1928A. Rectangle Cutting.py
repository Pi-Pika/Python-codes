t = int(input())

for i in range(0, t):
    a, b = [int(a) for a in input().split()]
    if a%2 == 0 and a/2 != b:
        print("YES")
    elif b%2 == 0 and b/2 != a:
        print("YES")
    else:
        print("NO")
