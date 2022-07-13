def tri_sum(arr):
    # start=0
    # end=len(arr)-1
    n=len(arr)
    a=[]
    i=0

    for i in range(0,n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):

                    if((arr[i]+arr[j]+arr[k]+arr[l])==8):
                        return([arr[i],arr[j],arr[k],arr[l]])
            
                
 
    return -1

arr=[2,2,2,2,2]
b=tri_sum(arr)
print(b)