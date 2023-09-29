arr = [[0]*5 for i in range(5)] # 2차원 배열 선언

for i in range(5): 
    a = 0
    if i < 4:
        for j in range(5):
            if j < 4:
                arr[i][j] = i * 4 + j + 1 # arr의 (i,j)좌표에 i * 4 + j + 1 값을 넣기
                a = a + i * 4 + j + 1  # i번 째 들의 값들을 누적
            else: # j가 5일때 
                arr[i][j] = a  # arr의 (i,5)에는 j가 1, 2, 3, 4 였을 때의 값들을 다 더한 값이 추가
                
    else:  # i값이 5일 때
        for k in range(5):
            b = 0
            for l in range(4):
                b = b + arr[l][k] 
            arr[i][k] = b  # b는 열이 k값이 었을 때의 l행값들의 합

for i in range(5):
    for j in range(5):
        print(arr[i][j], end = " ")
    print()


