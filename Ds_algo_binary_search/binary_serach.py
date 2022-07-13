letters=['c','f','g']
def binary_search(arr,target):
    low=0
    high=len(letters)-1

    while(low<=high):
        mid=int((low+high)/2)
        if (letters[mid]>target):
            high=mid-1
        else:
            low=mid+1
    
    return letters[low%len(letters)]



a=binary_search(letters,'y')
print(a)