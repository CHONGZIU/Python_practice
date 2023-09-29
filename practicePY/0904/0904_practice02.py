# 問題１
# 整数をx、yというintで入力
# ｘ > ｙの場合 ‐　xはyよりも大きい
# ｘ < ｙの場合 ‐　xがyよりも小さい
# ｘ = ｙの場合 ‐　xとyの値が同じ場合

x = input()
y = input()

if x > y:
    print ("xはyよりも大きい")
elif x < y:
    print ("xがyよりも小さい")
elif x == y:
    print ("xとyの値が同じ場合")