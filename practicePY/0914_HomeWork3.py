def student():
    num_student = input("The number of student. ")
    num_student = int(num_student)
    i = 0
    arr = []
    
    if num_student < 1 or num_student > 100:
        return
    
    while i != num_student:
        data = input("Name dd mm yyyy: ").split()
        if len(data[0]) > 15 or len(data[0]) < 0 or int(data[1]) > 31 or int(data[1]) < 1 or int(data[2]) > 12 or int(data[2]) < 1 or int(data[3]) > 2010 or int(data[3]) < 1990:
            continue
        else:
            arr.append({"name" : data[0], "day" : int(data[1]), "month" : int(data[2]), "year" : int(data[3])})
            i = i + 1
    
    for _ in range(0, len(arr)):
        for j in range(1, len(arr)):        
            if arr[j-1]["year"] > arr[j]["year"]:
                num = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = num
            if arr[j-1]["year"] == arr[j]["year"]:
                if arr[j-1]["month"] > arr[j]["month"]:
                    num = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = num
                if arr[j-1]["month"] == arr[j]["month"]:
                    if arr[j-1]["day"] > arr[j]["day"]:
                        num = arr[j]
                        arr[j] = arr[j-1]
                        arr[j-1] = num    
                        
student()
