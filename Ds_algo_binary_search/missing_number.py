def missingNumber(nums):
    n=len(nums)
    b=sorted(nums)
 
    for i in range(0,n):

        if(i!=b[i]):
            return i
            print(i)

def search(nums):
    a=missingNumber(nums)
    if(a==None):
        return len(nums)
arr=[0,1]
# arr=[2,0,7,5,8,1,4,6] 
b=search(arr)
print(b)
print(sorted(arr))