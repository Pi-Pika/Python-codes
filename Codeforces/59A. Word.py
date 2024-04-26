a = input()
upper = 0
lower = 0
for i in a:
    if (i.islower()):
        lower += 1
    else:
        upper += 1

if lower >= upper:
    print(a.lower())
else:
    print(a.upper())
