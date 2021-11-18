class employee:
    company="pubg"
    
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("employee is created")
    
    def getdetails(self):
        print(f"the name of employee is {self.name}")
        print(f"the salary of employee is {self.salary}")
        print(f"the subunit of employee is {self.subunit}")
    def getsalary(self):
        print(f"salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("hello sir ")


praneet=employee("praneet",15000,"phonepe")
# praneet.salary=15466
# praneet.getsalary()
# employee.getsalary(praneet)
# praneet.greet()
praneet.getdetails()