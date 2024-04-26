t = int(input())

for i in range(0, t):
    c = 0
    n = int(input())
    freq = {}
    a_list = [int(x) for x in input().split()]
    for a in a_list:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
    #print(freq)
    for i,j in freq.items():
        #print(freq[i], i, j)
        c += int(freq[i]/4)
    print(c)
