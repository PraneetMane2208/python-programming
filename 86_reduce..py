from functools import reduce

sum= lambda a,b:a+b
l= [2,5,5,3,9]
val=reduce(sum,l)
print(val)