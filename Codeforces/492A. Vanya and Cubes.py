a = int(input())
level = 0
c = 1
plus = 1
tot = 1
while 1:
    if tot > a:
        break
    plus += 1
    c += plus
    tot += c
    level += 1

print(level)
