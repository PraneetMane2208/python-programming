# def isPerfectSquare( num):
#     if not num:
#         return False                     it exceed time limit
        
#     for i in range(1, num+1):
#         square = i * i 
#         if square == num:
#             return True
#         elif square > num:
#             return False
# b=isPerfectSquare(16)
# print(b)




def isPerfectSquare( n):
        
    i = 1
    while(i * i<= n):
            
         
        # If (i * i = n)
        if (( (n % i == 0) and n / i == i)):
            return True
             
        i = i + 1
    return False
b=isPerfectSquare(25)
print(b)
