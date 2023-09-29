def function(**kwargs): # 受けた変数をkwargsというdictionaryに追加
    K = kwargs.get("x") # kwargsの中にあるxというキーをKという変数で入れる
    if K.isalpha() or -99 > int(K) or int(K) > 100: # Kが条件に当たるかを確認
        return function(x = input("値を入力してください")) # 間違ったときまた入力値を受ける
    K = int(K) # Kをint形で変わる
    if K >= 0 and K % 2 == 0: # Kが正のか負のかと偶数か奇数かを判別
        print("正の数の偶数")
    elif K >= 0 and K % 2 == 1:
        print("正の数の奇数")
    elif K < 0 and K % 2 == 0:
        print("負の数の偶数")
    else:
        print("負の数の奇数")

function(x = input("値を入力してください")) # functionを使ってxというキーと入力した値をバリューで受ける