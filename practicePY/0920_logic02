array = [5, 10, 7, 8, 3, 1, 9, 2]

def quick_sort(arr):
    p = arr[0]
    j = len(arr) -1
    i = 1
    num = 0
    while True:
        if p < arr[i] and p > arr[j]:
            num = arr[i] 
            arr[i] = arr[j]
            arr[j] = num
            j = j - 1
            i = i + 1
        elif p < arr[i] and p < arr[j]:
            j = j - 1
        elif p > arr[i] and p > arr[j]:
            i = i + 1
        elif p > arr[i] and p < arr[j]:
            j = j - 1
            i = i + 1
            
        if i > j :
            num = arr[0] 
            arr[0] = arr[j]
            arr[j] = num
            return arr

full = quick_sort(array)
h = int(len(full) / 2)
left = full[:h]
right = full[h:]

L = quick_sort(left)
R = quick_sort(right)

result = L + R
print(result)
