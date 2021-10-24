n = 4
# for i in range(1, n):
#     if(i%2==0):
#         print(" ")
#     else:
#         print("*" * (i))



# for i in range(1, n):
#     for j in range(1, n-i):
#         print(" ", end= ' ')
#     print("* " * (i))

center = int(n/2)
for i in range(1, n):
    for j in range(1, n-i):       
        print("#", end= ' ')
    if(center == i and center ==j):
        print("O", end= ' ')    
    else:
        print("* " * (i))