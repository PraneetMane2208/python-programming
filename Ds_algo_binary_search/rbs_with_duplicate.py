def search(nums,target):
    pivot=find_pivot_with_duplicates(nums)
    # if u do not find pivot then array is not rotated
    if(pivot==-1):
        # just do normal binary search
        return binary_search(nums,target,0,len(nums)-1)
    # if pivot is found u have two ascendind sorted arrays

    if(nums[pivot]==target):
        # return pivot
        return True



    if(target>=nums[0]):
        return binary_search(nums,target,0,pivot-1)
    return binary_search(nums,target,pivot+1,len(nums)-1)


def binary_search(nums,target,start,end):
    while(start<=end):
        mid=int(start+(end-start)/2)
        if (target<nums[mid]):
            end=mid-1
        elif(target>nums[mid]):
            start=mid+1
        else:
            return mid
    # return -1
    return False

def find_pivot_with_duplicates(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int(start+(end-start)/2)
        # 4 cases are over here
        if(mid<end and arr[mid]>arr[mid+1]):
            return mid

        if(mid>start and arr[mid]<arr[mid-1]):
            return mid-1
        if(arr[mid]==arr[start] and arr[mid]==arr[end]):
            # skip the duplicates
            # Note : what if the elements at start and end are pivot
            # check if start is pivot
            if(arr[start]>arr[start+1]):
                return start
                start+=1
            if(arr[end]<arr[end-1]):
                return end-1
                end-=1
        elif(arr[start]<arr[mid] or (arr[start]==arr[mid] and arr[mid]>arr[end])):
            start=mid+1
        else:
            end=mid-1
              
            
        

    return -1   
            
arr=[2,5,6,0,0,1,2]
b=search(arr,3)
print(b)