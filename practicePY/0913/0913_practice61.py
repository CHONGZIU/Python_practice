arr = [[0]*5 for _ in range(5)]
a = 0

for i in range(5):
    for j in range(5):
        if i == 0:
            a = a + 1
            arr[i][j] = a
        elif j == 4:
            a = a + 1
            arr[i][j] = a
    
        
for i in range(5):
    for j in range(5):
        print(arr[i][j], end = " ")
    print()