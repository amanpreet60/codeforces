n = int(input())
num = 0
for x in range(n):
    temp = input()
    if len(temp) == 3:
        if '++' in temp:
            num = num+1
        if '--' in temp:
            num = num-1
print(num)