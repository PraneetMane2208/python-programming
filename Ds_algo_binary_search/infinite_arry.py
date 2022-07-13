def binary_search(nums,target,start,end):
    
    while(start<=end):
        mid=int(start+(end-start)/2)
        if (target<nums[mid]):
            end=mid-1
        elif(target>nums[mid]):
            start=mid+1
        else:
            return mid

def range(nums,target):
    start=0
    end=1

    # first find the range
    #  first start with box of size 2
    while(target>nums[end]):
        new_start=end+1
        #double the box value
        #end=previous end + size of box*2
        end=end+(end-start+1)*2
        start=new_start
    return binary_search(nums,target,start,end)


nums=[3,5,7,9,10,90,100,130,140,160,170]
a=range(nums,5)
print(a)