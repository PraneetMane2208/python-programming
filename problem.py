num=int(input("enter your number:  "))
table=[num*i for i in range(1,11)]
print(table)
with open ("table.txt","a") as f:
    f.write(str(table))
    f.write('\n')

# problem no-2
# a=int(input("enter your number a:  "))
# b=int(input("enter your number b:  "))
# try:
#     print(a/b)
# except:
#     print('infinite')