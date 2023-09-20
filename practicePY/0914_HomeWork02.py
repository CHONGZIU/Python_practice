a = 0
arr = []
L = 0
A = 0
B = 0
Num = 0

def Number(N, M):
    while True:
        if int(N) < int(M):
            arr.append(N)
            break
        else:
            A = int(N) // int(M)
            B = int(N) % int(M) 
            arr.append(B)
            N = A      

    L = len(arr)
    for j in range(L - 1, -1 , -1):
        Num = arr[j]
        print(Num, end = "")
    return 

def result(d, e): 
    print("10진수: ", d)
    print("변환 : ", e)
    print("10 진수 ", d, "은/는 ", e, "진수 ", end = "")
    Number(d, e)
    print(" 입니다.")

result(input("数字を入力 "), input("進数を入力 "))