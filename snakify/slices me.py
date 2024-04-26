a = input()
l = len(a)

#1
print(a[2])
#2
print(a[-2])
#3
for i in range(0, 5):
    print(a[i], end="")
print()
#4
for i in range(0, l-2):
    print(a[i], end="")
print()
#5
for i in range(0, l):
    if i%2 == 0:
        print(a[i], end="")
print()
#6
for i in range(0, l):
    if i%2 != 0:
        print(a[i], end="")
print()
#7
for i in reversed(range(0, l)):
    print(a[i], end="")
print()
#8
j = 0
for i in reversed(range(0, l)):
    if j%2 == 0:
        print(a[i], end="")
    j += 1
print()
#9
print(l)
