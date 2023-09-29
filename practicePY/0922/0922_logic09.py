x = input()
x = int(x)
arr = []

while x > 0: # 分けることがないまでに分けるための反復門
    a = x % 2 # 残り
    arr.append(a) # 残りを配列に込む
    x = x // 2 # 分け前を変更    
    
for i in range(len(arr)-1, -1, -1): # 込んだ残りの配列を逆に出力するための反復門
    print(arr[i], end = "")
print()

for j in reversed(range(len(arr))): # 込んだ残りの配列を逆に出力するための他の反復門
    print(arr[j], end = "")