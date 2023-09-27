arr = []
for j in range(15):
    arr.append([])
    for i in range(15):
        arr[j].append(0)

for j in range(15):
    for i in range(15):
        if j == i:
            arr[j][i] = 1
            break
        elif i == 0:
            arr[j][i] = 1
        else:
            arr[j][i] = arr[j - 1][i - 1] + arr[j - 1][i]

for j in range(15):
    for i in range(15):
        if i == j:
            print(arr[j][i])
            break
        else:
            print(arr[j][i], end=" ")
            
            

