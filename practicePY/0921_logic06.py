list = [1, 2, 3, 4]

def line_up(arr, a): # a는 현재 순열의 시작위치
    if a == len(arr): # a가 arr의 길이와 같아질 때, 원소의 모든 순열을 생성한 경우
        print(arr) # 함수를 출력하고 종료
        return
    
    for i in range(a, len(arr)):
        arr[a], arr[i] = arr[i], arr[a]  # 순서를 바꾸어 다음 원소를 선택      
        line_up(arr, a + 1)  # 재귀 호출
        arr[a], arr[i] = arr[i], arr[a] 

line_up(list, 0)


