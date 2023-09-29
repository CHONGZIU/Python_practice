# 1~12の日数を表示
# 1~12以外の数字を入力する場合、'入力が間違っています'と表示

while True:
    m = input("月： ")
    try:
        m = int(m)
    except:
        print ("入力が間違っています")
        continue
    False
    
    if m == 2:
        print ("28日です")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print ("30日です")
    else:
        print ("31日です")
    break
        