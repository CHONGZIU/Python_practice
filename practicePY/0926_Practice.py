while True:
    input_1 = input("출점한 점포 수, 영업한 월 수: ").split()
    input_2 = input("건설비용, 인건비, 라멘 1개당 이익: ").split()
    N = int(input_1[0])
    M = int(input_1[1])
    A = int(input_2[0])
    B = int(input_2[1])
    C = int(input_2[2])
    
    if N < 1 or N > 1000 or M < 1 or M > 12 or A < 1 or A > 10000 or B < 1 or B > 10000 or C < 1 or C > 500:
        continue
    else:
        break

count = 0
i = 1

while i <= N:
    R_i = int(input("M개월간 판매한 라멘의 개수: "))
    if 1 > R_i or 1200 < R_i: 
        continue
    else:
        income = C * R_i - A - B * M # 라멘 한개당 이익 * 라멘 판매수 - 건설비용 - 인건비 * 영업기간
        i += 1
        if income < 0:
            count = count + 1
print(count)
