# filter syntax - list(filter(function,list))

def greater_than_4(num):
    if num>4:
        return True
    else :
        return False

l=[2,5,7,34,67,3,1,4,6,8,0,7,45]
print(list(filter(greater_than_4,l)))