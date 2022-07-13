def sqrt(x):

    ans=-1
    i=1
    while(i*i<x):
        if(x%i==i):
            return i
        else:
            value=x/i
            ans=i
        i+=1
    return ans
a=sqrt(3)
print(a)