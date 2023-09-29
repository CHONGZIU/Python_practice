# 奇数合計
S = 0
I = 1

while I <= 100:
    S = S + I
    I = I + 2
print(S)
 

# 偶数合計
E = 0

for I in range(0,101):
    E = E + I
    I += 2
print(E) 