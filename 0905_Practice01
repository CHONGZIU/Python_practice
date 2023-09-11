#｛30, 355, 24, 12, 98, 72, 5, 76, 60, 35, 54, 62, 2, 12, 35｝昇順にソート　→　挿入ソート

arr = [30, 355, 24, 12, 98, 72, 5, 76, 60, 35, 54, 62, 2, 12, 35]

l = len(arr)
for j in range(0,l):
    for i in range(1, l-j):
        if arr[i-1] > arr[i]:
                num = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = num
        
print (arr)

# ジユンさん
number = [30, 355, 24, 12, 98, 72, 5, 76, 60, 35, 54, 62, 2, 12, 35]

for x in range(1, len(number)):
    temp = number[x]
    n = x - 1
    
    while (n >= 0) and (number[n] > temp):
        number[n+1] = number[n]
        n -= 1
        number[n+1] = temp
        
print("number =>", number)