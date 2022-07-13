def nextgreatestletter(letters,target):
    st=0
    end=len(letters)-1
    while(st<=end):
        mid=int(st+(end-st)/2)
        if(letters[mid]>target):
            end=mid-1
        else:
            st=mid+1
    return letters[st%len(letters)]
arr=['c','f','g']
b=nextgreatestletter(arr,'z')
print(b)