class employee:
    
    company="google"
    def showdetail(self):
        print("this is an employee")

class programmer(employee):
    language="python"


    def getlanguage(self):
        print(f"the language is {self.language}")

    def showdetail(self):
        print("this is an programmer")


e=employee()
e.showdetail()

p=programmer()
p.showdetail()
p.getlanguage()