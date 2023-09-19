def birthday(N, D, M, Y):
    if len(N) > 15:
        return
    if int(D) < 1 or int(D) > 31:
        return
    if int(M) < 1 or int(M) > 12:
        return
    if int(Y) < 1990 or int(Y) > 2010:
        return
    return (N, int(Y), int(M), int(D))
    
def student():
    S = input("The number of student. ")
    S = int(S)
    if S < 1 or S > 100:
        return
    arr = []
    for _ in range(S):
        arr.append(birthday(input("name "), input("day "), input("month "), input("year ")))
    max = arr.pop()
    min = max
    for i in range(0, len(arr)):
        if compare_student(arr[i], max) > 0:
            max = arr[i]
        if compare_student(arr[i], min) < 0:
            min = arr[i]
    
    print("old : ", min[0])
    print("young : ", max[0])

def compare_student(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    if a[2] > b[2]:
        return 1
    elif a[2] < b[2]:
        return -1
    if a[3] > b[3]:
        return 1
    elif a[3] < b[3]:
        return -1
    return 0

if __name__ == "__main__": # 직접 실행했을 때만 실행된다.
    student()
