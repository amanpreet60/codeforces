n = int(input())
arr = []
for x in range(n):
    arr.append(input())
for y in arr:
    if len(y) > 10:
        print(y[0]+str(len(y)-2)+y[-1])
    else:
        print(y)
    