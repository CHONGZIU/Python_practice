def information(number):
    user_arr = []
    x = 0
    while x < number:
        
        name, dd, mm, yyyy = input("유저의 name dd mm yyyy를 입력해주세요. ").split() # 입력받은 값을 공백을 기준으로 분리
        
        if len(name) > 15 or (int(dd) < 0 or int(dd) > 31) or (int(mm) < 0 or int(mm) > 12) or (int(yyyy) < 1990 or int(yyyy) > 2010):
            continue
        else:
            user = {"name" : name, "dd":int(dd), "mm":int(mm), "yyyy" : int(yyyy)} # 받은 값을 한꺼번에 딕셔너리로 만들어서
            user_arr.append(user) # 그 딕셔너리를 배열안에 넣기
            x += 1

    user_arr = Insertion_Sort(user_arr) # 정렬

    print("나이가 가장 적은 사람", user_arr[0]["name"])
    print("나이가 가장 많은 사람", user_arr[len(user_arr)-1]["name"])

def Insertion_Sort(arr): # 정렬하는 메소드 선언
    for x in range(1, len(arr)):
        current_user = arr[x]
        j = x - 1
    
        while j >= 0 and (arr[j]["yyyy"], arr[j]["mm"], arr[j]["dd"]) < (current_user["yyyy"], current_user["mm"], current_user["dd"]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_user
        
    return arr

def number_check(number):
    if number.isalpha():
        return number_check(input("학생의 수를 다시 입력해주세요"))
    else : 
        information(int(number))
        
number_check(input("학생의 수를 입력해주세요")) 

