n = input().split(' ')
num = 0
for x in range(int(n[0])):
    if num <= int(n[1]):
        temp = int(input())
        if temp>0:
            num += 1
    else:
        if int(input()) == temp and temp>=0:
            num += 1
print(num)


# CG241219V6576486