Name, Kor, Eng, Math = input().split()
# 合格/ 不合格, 理由: 平均未満 /不合格, 理由: 科落.
Kor = int(Kor)
Eng = int(Eng)
Math = int(Math)
average = (Kor + Eng + Math)/3
average = round(average,2)
result = ""
reason = ""

if Kor and Eng and Math >= 40 and average >= 60: #한꺼번에 비교하는 법 찾아보기
    result = "합격"
elif average < 60:
    result = "불합격"
    reason = "평균 미만"
elif Kor or Eng or Math < 40:
    result = "불합격"
    reason = "과락"

print("이름: ", Name)
print("평균: ", average)
print("판정: ", result)
print("불합격사유: ", reason)
