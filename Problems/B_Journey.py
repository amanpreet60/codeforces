n = input()
for x in range(int(n)):
    a = list(map(int, input().split()))
    distance = a[0]
    i = 1
    sum = a[1] + a[2] + a[3]
    initial = int((distance/sum))*3
    initial2 = int((distance/sum))*sum
    while initial2 < distance:
        initial2 = initial2 + a[i]
        i += 1
        initial += 1
    print(initial)

