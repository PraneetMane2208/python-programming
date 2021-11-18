a=[45,68,69,25,64,35,36,2,5,8,61,35,12.14]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

b=[i for i in a if i%2==0]    # shortcut method 
print(b)