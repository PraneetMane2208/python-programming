class person:
    country="india"
    def __init__(self):
        print("initialising person")

    def takebreak(self):
        print("eating momos")

class employee(person):
    company="phonpe"
    def __init__(self):
        # super().__init__()
        print("initialising employee")   
    def takebreak(self):
        super().takebreak()
        print("drinking tea")

    def getsalary(self):
        print(f"salary is {self.salary}")


class programmer(employee):
    company="gs lab"
    def __init__(self):
        super().__init__()
        print("initialising programer")

    def getsalary(self):
        print(f"no salary only duty")
    def takebreak(self):
        print("playing ball")    

        super().takebreak()
# p=person()
# e=employee()
pr=programmer()
# p.takebreak()
# e.takebreak()
# pr.takebreak()


# print(e.company)
# print(pr.country)