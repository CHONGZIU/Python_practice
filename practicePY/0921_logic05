# 複数の数値ー＞最小公倍数、最大公約数
# 素数まで

def gcd(a, b): # 最大公約数を求める関数
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(l, m): # 最小公倍数を求める関数
    return int(l * m / gcd(l, m))

def list_gcd(list): # 最大公約数
    for _ in range(1, len(list)): # リストの数より１小さい番目で反復
        arr = [] # 配列の中にある数字を比較して出た公約数を込むための配列を作る
        for i in range(1, len(list)): # 配列の中にある数字を一々比較するための反復門
            arr.append(gcd(int(list[i-1]), int(list[i]))) # 比較した後出た公約数をarrに込む
        list = arr # また、リストの中にある数字たちの公約数を求めるためにリストをarrで変わる
    print(list[0]) # 最終でリストに残った数字が最大公約数

def list_lcm(list):# 最小公倍数
    for _ in range(1, len(list)): # リストの数より１小さい番目で反復
        arr = []# 配列の中にある数字を比較して出た公倍数を込むための配列を作る
        for n in range(1, len(list)): # 配列の中にある数字を一々比較するための反復門
            arr.append(lcm(int(list[n-1]), int(list[n]))) # 比較した後出た公約数をarrに込む
        list = arr # また、リストの中にある数字たちの公倍数を求めるためにリストをarrで変わる
    print(list[0]) # 最終でリストに残った数字が最大公倍数


x = input("値を入力してください")

list = x.split()
list_gcd(list)
list_lcm(list)