def arrangeCoins( n: int) -> int:
        total = 0
        i = 1
        
        while n >= i:
            n-=i
            total+=1
            i+=1
               
        return total

b=arrangeCoins(56)
print(b)