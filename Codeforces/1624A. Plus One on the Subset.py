t = int(input())
i = 0
while 1:
    if i == t:
        break
    i += 1
    a = int(input())
    a_list = list(map(int, input().split()))
    ma = max(a_list)
    mi = min(a_list)
    print(ma-mi)
