t = int(input())

for i in range(0, t):
    a, b = [int(x) for x in input().split()]
    b = int(b/2)
    print(b*a)

