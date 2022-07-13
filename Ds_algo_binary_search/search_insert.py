def binary_search(arr,target):
     
     start=0
     end=len(arr)-1
     while(start<=end):
        mid=int(start+(end-start)/2)
        if (target<arr[mid]):
            end=mid-1
        elif(target>arr[mid]):
            start=mid+1
        else:
            return mid
     return -1
def insert(arr,target):
    b=binary_search(arr,2)
    start=0
    end=len(arr)-1
    if(b==-1):
        while(start<=end):
            mid=int(start+(end-start)/2)
            if(target>arr[mid]):
                start=mid+1
            if(target<arr[mid]):
                end=mid-1
            if(start==end):
                #c=start+1
                return start+1
        # b=arr.insert(c,target)
        # return arr

                # return arr.insert(start+1,target)
    else:

        return binary_search(arr,target)
arr=[1,3,5,6]
c=insert(arr,2)
print(c)

