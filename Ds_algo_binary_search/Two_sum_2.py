arr=[2,7,11,15]
# n=4
# target=17
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):

#         if(arr[i]+arr[j])==target:

#             b= (i,j)
#             print(b)

# second_method
def twoSum (numbers, target):
        
        low=0
        high=len(numbers)-1
        while(low<high):
            if((numbers[low]+numbers[high])>target):
                high=high-1
            elif((numbers[low]+numbers[high])<target):
                low=low+1
            else:
                return [low,high]
b=twoSum(arr,17)
print(b)