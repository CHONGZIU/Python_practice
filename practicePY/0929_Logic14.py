num = input("数字を２つ入力してください。 ").split() # まず、入力された数字をnumというlistで作る

while True: # 入力された数字が正しい数字なのかを検討
    if num[0].isalpha() or int(num[0]) < 0:
        num = input("数字を直してください。 ").split()
    elif num[1].isalpha() or int(num[1]) < 0:
        num = input("数字を直してください。  ").split()
    else:
        break

for i in range(2, int(num[0]) + 1): # 二つの数字の中に公約数があったら"お互いに素でありません。"と出力、ないなら"お互いに素であります。"と出力
    if (int(num[0]) % i == 0) and (int(num[1]) % i == 0):
        print("お互いに素でありません。")
        break
    elif i == int(num[0]):
        print("お互いに素であります。")
        



