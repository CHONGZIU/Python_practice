def compare(a): # 入力値が条件に当たるかを判断する関数
    if a.isalpha(): # 変数が文字なのか数字なのかを判断するため
        return True
    a = int(a) # 変数をintに変わる
    if 0 > a or a > 100:
        return True
    return False

while True: # 入力値Xに正しい値が入るまでの反復門
    x = input("Xの値を入力してください。")
    m = compare(x)
    if m == False:
        break # ループを止める

while True: # 入力値Yに正しい値が入るまでの反復門
    y = input("Yの値を入力してください。")
    n = compare(y)
    if n == False:
        if x > y: # Yだけの条件を確認
            print(x, "は", y, "よりも大きい")
            break # ループを止める

        