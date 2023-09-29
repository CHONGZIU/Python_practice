# 32
A = input()
A = int(A)
I = 2

while I < A:
    N = A - int(A / I) * I
    I = I + 1
    if N == 0:
        break
        
if A == I:
    print("소수")
else:
    print("소수 아님")