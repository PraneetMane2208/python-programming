# s = {25,25.0,"25"}
# print(len(s))        # 20 and 20.0 is counted only once


# a  = int(input("enter a first number:\n "))
# b  = int(input("enter a second number:\n "))
# c  = int(input("enter a third number:\n "))
# d  = int(input("enter a fourth number:\n "))
# s = {a,b,c,d}
# print(s)



s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))