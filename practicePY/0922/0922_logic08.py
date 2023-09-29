# １００円、１０円、５円、１円で分ける

def cal(kane = input("金を入力してください")):
    list = [100, 10, 5, 1] # 入る金の数のための配列
    kane = int(kane) # 金はstrで入るから、あれをintで変更
    for i in range(0, len(list)): # list全てで分けるための反復門
        a = int(kane / list[i]) # aはできるだけ少ない枚数、あれが分け前
        print(list[i],"円: " , a)    
        kane = kane % list[i] # 次の配列の数で残ってる金を分けるためkaneを残りで変わる

cal()