#星を積む
cnt = 1

for i in range (0, 9):
    if cnt < 9 and i < 5:
        for j in range (0, 4-i):
            print (" ", end = "")
    else:
        for j in range (0, i - 4):
            print (" ", end = "")
    
    for z in range (0, cnt):
        print ("*", end = "")
    print ()
    
    if cnt < 9 and i < 5:
        cnt += 2
    else:
        cnt -= 2
                


#j = 5

#for n in range (0,j):
#    print (" " * (j - 1 - n), end = "")
#    print ("*" * ( 2 * n + 1)) 

#for n in range ((j-1),0,-1):
#    print (" " * (j - n), end = "")
#    print ("*" * (2 * n - 1)) 
