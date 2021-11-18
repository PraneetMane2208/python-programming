class number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):

        print(self.num)
        print(num2.num)
        return self.num+num2.num

    # def __add__(self,a1,a2):

    #     print("lets add")
    #     return self.num+a1.num+a2.num
n1=number(5)
n2=number(7)
#n3=number(8)
sum = n1+n2
# print(sum)
print(sum)