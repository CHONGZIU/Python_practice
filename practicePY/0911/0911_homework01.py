money = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

I = input()
I = int(I)
l = len(money)

for i in range(0,l):
    a = int(I / money[i])
    I = I - money[i] * a
    print(money[i], "원", a)
    
    