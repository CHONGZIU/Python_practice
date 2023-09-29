arr = [] 
for j in range(15): # ２次元の配列を作る
    arr.append([])
    for i in range(15):
        arr[j].append(0)

for j in range(15): # jは行
    for i in range(15): # iは列
        if j == i: # jとiが同じ時数字1を書く
            arr[j][i] = 1
            break
        elif i == 0: # iが0になったら、また1を書く
            arr[j][i] = 1
        else: # その以外のところは上とうえの左にある数字を加えた数字を書く
            arr[j][i] = arr[j - 1][i - 1] + arr[j - 1][i]

for j in range(15): # 配列の中の数字を欲しい形で出力する
    for i in range(15):
        if i == j:
            print(arr[j][i])
            break
        else:
            print(arr[j][i], end=" ")
            
            

