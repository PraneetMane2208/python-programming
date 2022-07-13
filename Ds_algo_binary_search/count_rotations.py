#from Ds_algo_binary_search.rbs_with_duplicate import find_pivot


def rotation_count(arr):
    pivot=find_pivot(arr)
    return pivot+1


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
def find_pivot(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int(start+(end-start)/2)
        # 4 cases are over here
        if(mid<end and arr[mid]>arr[mid+1]):
            return mid

        if(mid>start and arr[mid]<arr[mid-1]):
            return mid-1
        if(arr[mid]<=arr[start]):
            end=mid-1
        else:
            start=mid+1

    return -1         
arr=[4,5,6,7,0,1,2]
b=rotation_count(arr)
print(b)