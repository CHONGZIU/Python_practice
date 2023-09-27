while True: # 正しい値を受けるための反復門
    number = input("?? ")
    if number.isalpha(): # 入力された値が条件に当たるのかどうかを検討すること
        continue
    else:
        number = number.split() # 正しい値が入れたらあれを空白を基準して分離する
        break
    
for j in range(0,4): # 配列の中で数字を手順に整理するための反復門
    for i in range(1,4):
        if int(number[i-1]) > int(number[i]):
            number[i-1], number[i] = number[i], number[i-1]

print(number[2]) # この配列のなかの二番目の配列が３番目で大きい数字