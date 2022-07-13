def findKthPositive( arr, k):
        b=[]
        j=1
        i=0
        while(i<len(arr)):
            if(arr[i]!=j):
                b.append(j)
                j+=1
            else:
                i+=1
                j+=1
                
        return b[k-1]
arr=[1,2,3,4]
b=findKthPositive(arr,5)
print(b)