t = int(input())

for j in range(0, t):
    n = int(input())
    s = input()
    ans = 0
    to = n
    c = 0
    for i in range(0, n-1):
        if s[i] == '*' and s[i] == s[i+1]:
            to = i
            c = 1
        if c == 1:
            break
        print(to)
    for k in range(0, to+1):
        if s[k] == '@':
            ans += 1
    print(ans)
