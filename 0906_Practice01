# 何周年のか計算してください。
def number1_Chk(num1):
    if not num1.isdigit():
        return False
    elif int(num1) < 1900 or int(num1) > 2022:
        return False
    else:
        return True
    
def number2_Chk(num1, num2):
    if not num2.isdigit():
        return False
    elif int(num2) < 1900 or int(num2) > 2022:
        return False
    elif int(num2) < num1:
        return False
    else:
        return True
    
num1 = input("入力してください。")
value = number1_Chk(num1)

while not value:
    num1 = input("値をもう一度入力してください。")
    value = number1_Chk(num1)

num1 = int(num1)
num2 = input("入力してください。")
value = number2_Chk(num1, num2)

while not value:
    num2 = input("値をもう一度入力してください。")
    value = number2_Chk(num1, num2)
    
num2 = int(num2)

if num2 > num1:
    print(num2 - num1)
else:
    print(num1 - num2)    