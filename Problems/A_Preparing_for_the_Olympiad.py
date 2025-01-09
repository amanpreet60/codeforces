n = input()
for x in range(int(n)):
    sum = 0
    t = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for x in range(t-1):
        temp = a[x]-b[x+1]
        if(temp > 0):
            sum = sum + temp
    print(sum+a[-1])

