t = int(input())

for i in range(0, t):
    n = int(input())

    for ind, j in enumerate(a_list):
        if ind%2 == 0:
            a += min(a_list[ind], a_list[ind+1])
    print(a)
