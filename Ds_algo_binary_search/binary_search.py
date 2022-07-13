def search( nums, target):
        if(len(nums)==1):
            if(nums[0]==target):
                return len(nums)-1
            else:
                return -1
        else:
            start=0
            end=len(nums)-1
            while(start<end):
                mid=start+(end-start)/2
                if(nums[mid]==target):
                    return mid
                elif(nums[mid]>target):
                    end=mid-1
                else:
                    start=mid+1
            return -1

nums=[2,5]
a=search(nums,5)
