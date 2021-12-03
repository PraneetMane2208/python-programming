# l = [1,36,98]
# for item in l : print(item)




# for i in range (1,8,2) : print(i)

# optinal else
class student:
    name =''
    age = ''
    def __init__(self, name, age):
        self.name = name
        self.age=age
a = student("pavan", 25)
b = student("pranit", 18)

l = [a,b]
for item in l :
    print(item.name)
