# 31
S = 0
T = 0

for I in range(1, 101):
    if I / 2 == int(I/2):
        T = T + I # 偶数合計
    else:
        S = S + I # 奇数合計

print(S, T)