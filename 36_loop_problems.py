# num = int(input("enter your number :"))
# for i in range(1,11):
    # print(str(num) + "*" +str(i)+ "="+str(i*num))



    # PROBLEM NO- 2

# L =["sohan","sachin","rahul","sandhu"]

# for name in L:
    # if name.startswith("s"):
        # print("hello" + name)


        # problem no - 3

num = int(input("enter your number :"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime = False 
        break
if prime:
    print("this number is prime")
else :
    print("this number is not prime")
        