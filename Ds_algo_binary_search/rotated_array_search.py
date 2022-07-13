def mountain_array(arr):
    start=0
    end=len(arr)-1
    while(start<end):

        mid=int(start+(end-start)/2)
        if(arr[mid]>arr[mid+1]):
            end=mid
        else:
            start=mid+1
    return start

def order_agnostic(nums,target,flag,start,end):
    if(flag==1):
        ans=-1
        
        # start=0
        # end=len(nums)-1
        while(start<=end):
            mid=int(start+(end-start)/2)
            if (target<nums[mid]):
                end=mid-1
            elif(target>nums[mid]):
                start=mid+1
            else:
                ans=mid
                end=mid-1
    else:
        ans=-1
        
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=int(start+(end-start)/2)
            if (target<nums[mid]):
                end=mid-1
            elif(target>nums[mid]):
                start=mid+1
            else:
                ans=mid
                start=mid+1

            
                
    return ans

def search(arr,target):
    peak=mountain_array(arr)
    firsttry=order_agnostic(arr,target,1,0,peak)
    if (firsttry!=-1):
        return firsttry
    else:
        return order_agnostic(arr,target,0,peak+1,len(arr)-1)

arr=[3,4,5,6,7,0,1,2]
b=search(arr,0)
print(b)