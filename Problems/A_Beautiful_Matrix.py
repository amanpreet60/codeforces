arr = []
count = 0
loc = [0,0]
for i in range(5):
    arr.append(list(input().replace(" ","")))
    for j in range(5):
        if '1' in arr[i][j]:
            loc = [i,j]
print(abs(2-loc[0])+abs(2-loc[1]))