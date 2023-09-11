# 整数７つを入力
# 最大値、最小値以外の値を加えて出力
# 挿入ソート使って
list = list(map(int, input().split()))
L = len(list)
num = int()
x = int()

for i in range(1, L):
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            num = list[j-1]
            list[j-1] = list[j]
            list[j] = num

for r in range(1,L-1):
    x = x + list[r]
    
print("입력점수: ", list)
print("최대점수: ", list[L-1])
print("최소점수: ", list[0])
print("합계(최대-최소): ", x)