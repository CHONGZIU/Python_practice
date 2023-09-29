# A와 B와 최소 공배수를 구하는 프로그램을 작성하시오.

def input_testcase(C):
    C = int(C)
    if C < 1 or C > 1000:
        return input_testcase(input("테스트의 개수를 다시 입력하세요"))
    return C

def input_test(T):
    list = T.split()
    x = int(list[0])
    y = int(list[1])
    if x < 1 or x > 45000 or y < 1 or y > 45000:
        return input_test(input("테스트의 값을 다시 입력하세요"))
    return x, y

def gcd(a, b): # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(l, m): # 최소공배수
    return l * m / gcd(l, m)

def cal():
    A = input_testcase(input("테스트의 개수를 입력하세요"))
    for _ in range(A):
        B = input_test(input("테스트의 값을 입력하세요"))
        c = B[0]
        d = B[1]
        print(int(lcm(c, d)))
    return

cal()
