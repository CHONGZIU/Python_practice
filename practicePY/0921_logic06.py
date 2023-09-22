list = [1, 2, 3, 4]

def line_up(arr, a): # aは現在順列の始まる位置
    if a == len(arr): # aがarrの長さと同じようになった時、配列中の数字、全部順列を生成した場合
        print(arr) # 関数を出力して終わり
        return
    
    for i in range(a, len(arr)):
        arr[a], arr[i] = arr[i], arr[a] # 手順を変わって次の数字を選ぶ
        line_up(arr, a + 1) # 再帰呼び出す
        arr[a], arr[i] = arr[i], arr[a]  


line_up(list, 0)


