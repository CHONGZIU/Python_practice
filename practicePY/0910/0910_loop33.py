# 33 : 
M = input()
M = int(M)

K = 0

for I in range(2, M):
    I += 1
    for J in range(2, I):
        print(J)
        J += 1
        N = I - int(I / J) * J 
        if N == 0:
            break
    if I == J:
        K = K + 1

print(K)