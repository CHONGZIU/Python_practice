import random

com = random.randrange(0, 100) # 数字を無作為で一つ選ぶ
count = 0 # 何回目で当たるのかを数える変数

while True:
    user = input("数字を入力してください") # ユーザが入力する数字
    if user.isalpha() or int(user) < 0 or int(user) > 100: # ユーザが入力した数字が正しいのかを検討
        continue
    else: # 正しい数字ならこちらで
        count += 1 # ユーザが何回目で当たるのかを数える
        if com == int(user): # 数字が一致したら、下の実行門を実行して反復門を抜く
            print("computer: ", com)
            print("user: ", user)
            print(count, "回目で正解")
            break
        elif com > int(user): # ユーザの数字が大きいなら下の文章を出力
            print("comの値がユーザの値より大きい。")
        else: # ユーザの数字が小さいなら下の文章を出力
            print("ユーザの値がcomのより小さい。")
        continue # 数字が当たるまでに反復
