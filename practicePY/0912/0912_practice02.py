arr = [] # 배열 선언

for i in range(5): # i는 행의 번째
    arr.append([])  # arr라는 배열안에 또 배열을 추가
    a = 0
    if i < 4:
        for j in range(5): # j는 열의 번째
            if j < 4: # j는 4일 때까지 순서대로 숫자를 찍는다
                arr[i].append(i * 4 + j + 1)  # arr의 i번째 배열안에 괄호 안의 값을 넣는다
                a = a + i * 4 + j + 1
            else: # j가 5일 때는 1부터 4까지의 합
                arr[i].append(a) # 

    else:  # i가 5일 때는 열들의 합을 구해야 한다 
        for k in range(5):  # k는 열의 번째
            b = 0
            for l in range(4):  # l은 행의 번째
                b = b + arr[l][k] # (l,k)의 값을 누적
            arr[i].append(b) # arr의 i번째 배열에 b를 적는 다

for i in range(5): # 배열을 5개씩 끊어서 출력하는 식
    for j in range(5):
        print(arr[i][j], end = " ")
    print()