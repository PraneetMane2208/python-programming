# def singleNonDuplicate( nums):

        
       
#     for i in range(0,len(nums),2):
#         if(len(nums)==1):
#             return nums[0]
#         if(i==len(nums)-1 and nums[i]!=nums[i-1]):

#             # if(nums[i]==nums[i-1]):
#             return nums[i]
#         if(i<(len(nums)-1)and nums[i]!=nums[i+1]):
#             return nums[i]
#         # if(i==len(nums)-1 and nums[i]==nums[i-1]):
#         #     if(nums[i]==nums[i-1]):
        #         return nums[i]
def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]
            
       
            

nums=[2,2,3,3,4,4,8]
b=singleNonDuplicate(nums)
print(b)