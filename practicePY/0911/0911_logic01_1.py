def compare(a):
    if a.isalpha():
        return "NO"
    a = int(a)
    if 0 > a or a > 100:
        return "NO"
    return "YES"

while compare(input()) == "YES":
    x = input("X의 값을 입력하시오")
    m = compare(x)
    while compare(input()) == "YES":
        y = input("Y의 값을 입력하시오")
        n = compare(y)
        if x > y:
            print(x, "는", y, "보다 큽니다")
            break
        