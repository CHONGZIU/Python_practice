# 整数７つを入力
# 最大値、最小値以外の値を加えて出力

a, b, c, d, e, f, g = input().split()
value = [a, b, c, d, e, f, g]
list = list(map(int, value))
N = len(list)
Num = 0
x = 0

for j in range(N): # range(中に変数で処理)
    for i in range(0,N-1):
        if list[i] > list[i+1]:
            Num = list[i+1]
            list[i+1] = list[i]
            list[i] = Num
            
for l in range(1,N-1):
    x = x + list[l]

print("입력점수 : " , a, b, c, d, e, f, g)
print("최대점수 : " , list[6])
print("최소점수 : " , list[0])
print("합계(최대-최소) : " , x)