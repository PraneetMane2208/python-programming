n =7 
center = int(n/2) # center =1
for i in range(n): #i=0
    for j in range(n): #j=0 
        if (i ==center and j ==center):
            print(" " ,end =' ')
        else:
            print("*" ,end =' ')
    print() #bring to new line because end value is '\n'