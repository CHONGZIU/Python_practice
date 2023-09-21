arr = [5, 10, 7, 8, 3, 1, 9, 2]

def quick_sort(array): # 関数を作る
    left = [] # 基準値より小さい数字を込むリスト
    right = [] # 基準値より大きい数字を込むリスト
    
    if len(array) <= 1:  # 再帰関数を終わるための条件
        return array
    
    p = array[0] # 配列の中の数字を比較するための数字をpという変数で決める
    
    for i in range(1, len(array)): # 配列の数字をｐを基準して小さい数はleft、大きい数はrightに込むための反復門
        if p > array[i]:
            left.append(array[i])
        else:
            right.append(array[i])
    
    return quick_sort(left) + [p] +  quick_sort(right) # 再帰反復門を使って関数を継続に進めて、最後に整理できた数字を集める

print(quick_sort(arr))
