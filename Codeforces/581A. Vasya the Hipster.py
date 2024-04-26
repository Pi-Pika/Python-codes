a, b = [int(a) for a in input().split()]

print(min(a, b), int((max(a, b)-min(a, b))/2))
