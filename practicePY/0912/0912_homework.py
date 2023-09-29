def compare(y): # 変数を条件を検討するための関数
    if y.isalpha(): # 変数が文字なのか数字なのかを検討
        return True
    else:
        y = int(y) # 変数をint形に変更
    if -99 > y or y > 100: # 変数が範囲の中にあるのかないのかを検討
        return True
    return False

while True: # 無限ループを作る
    x = input("値を入力してください。") # 入力値を受ける
    z = compare(x) # 関数に入力値を入れて、あれを他の変数で宣言
    if z == False: # ｘが条件に当たるとループを脱出
        x = int(x)
        break
    
if x >= 0: # 変数の条件による正しい値を出力
    print("正の数の奇数か偶数か")
else:
    print("負の数の奇数か偶数か")
