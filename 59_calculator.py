class calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"the square of {self.num} is {self.num **2}")

    def cube(self):
        print(f"the cube of {self.num} is {self.num **3}")

    def squareroot(self):
        print(f"the square root of {self.num} is  {self.num**.5}")

a=calculator(5)
a.square()
a.cube()
a.squareroot()