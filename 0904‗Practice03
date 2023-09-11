# 整数をx、yというintで入力
# ＋なら、整数をx、yというintで入力
# －なら、負の数の奇数か偶数か

m = True
z = None
while m:
    z = input()
    try:
        z = int(z)
    except:
        print ("값을 다시 입력하시오")
        continue
    m = False
    
if z >= 0: 
    if z % 2 == 0:
        print ("z는 양의 짝수")
    else:
        print ("z는 양의 홀수")
elif z < 0:
    if z % 2 == 0:
        print ("z는 음의 짝수")
    else:
        print ("z는 음의 홀수")