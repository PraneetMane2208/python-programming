from functools import reduce

l = [3,7,55,8,7,3,5,66,7,7,99,77,666,788]
a=reduce(max,l)
print(a)