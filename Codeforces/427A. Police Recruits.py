t = int(input())
crime = 0
police = 0

a_list = list(map(int, input().split()))

for a in a_list:
    if a == -1:
        if police != 0:
            police -= 1
        else:
            crime += 1
    else:
        police += a

print(crime)
