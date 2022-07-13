import math


def judgeSquareSum( c):
        
    left = 0
    right = int(math.sqrt(c))
    while left <= right:
        cur = left * left + right * right
        if cur == c: return True
        if cur < c:
            left += 1
        else:
            right -= 1
    return False
c=29
b=judgeSquareSum(c)
print(b)
    
        
   