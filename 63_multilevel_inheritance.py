class person:
    country="india"
    def takebreak(self):
        print("eating momos")

class employee(person):
    company="phonpe"
    def takebreak(self):
        print("drinking tea")

    def getsalary(self):
        print(f"salary is {self.salary}")


class programmer(employee):
    company="gs lab"
    def getsalary(self):
        print(f"no salary only duty")
    def takebreak(self):
        print("playing ball")    

p=person()
e=employee()
pr=programmer()
p.takebreak()
pr.takebreak()
print(e.company)
print(pr.country)
