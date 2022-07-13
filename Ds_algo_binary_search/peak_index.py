def peakIndexInMountainArray( arr):
        start=0
        end=len(arr)-1
        while(start<=end):
            mid=int(start+(end-start)/2)      # difrent mtd to find out mountain array
            if(arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid]<arr[mid-1]):
                return mid-1
            else:
                start+=1
arr=[1,2,1,3,5,6,4]
b=peakIndexInMountainArray(arr)
print(b)