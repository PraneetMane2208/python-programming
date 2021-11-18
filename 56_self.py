class employee:
    company="pubg"
    def getsalary(self):
        print(f"salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("hello sir ")


praneet=employee()
praneet.salary=15466
# praneet.getsalary()
employee.getsalary(praneet)
praneet.greet()