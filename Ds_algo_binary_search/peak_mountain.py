a=[1,2,3,7,6,3,2]
def mountain_array(arr):
    start=0
    end=len(a)-1
    while(start<end):

        mid=int(start+(end-start)/2)
        if(arr[mid]>arr[mid+1]):
            end=mid
        else:
            start=mid+1
    return start

b=mountain_array(a)
print(b)