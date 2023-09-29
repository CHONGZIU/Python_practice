arr = [0, 1] # 計算のために配列の0，1番目の数字が入っている配列を宣言

for i in range(0, 48): # 配列を50個まで入れるための反復門
    num = arr[i] + arr[i+1] # iとi+1番目を加えた数字i+2番目の数字
    arr.append(num) # 計算した数字を配列に入れる

print(arr)
    