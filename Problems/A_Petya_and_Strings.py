str1 = input()
str2 = input()
i = 0
for x in str1:
    if x.lower() > str2[i].lower():
        print(1)
        exit()
    elif x.lower() < str2[i].lower():
        print(-1)
        exit()
    else:
        i += 1
print(0)
    