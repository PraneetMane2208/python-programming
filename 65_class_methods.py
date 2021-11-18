class employee:
    company="zerodha"
    salary=1000
    location="bk"

    # def changesalary(self,sal):
    #     self.__class__.salary=sal     # its one method to change the class salary 
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal              # second method and it is easy to directly change classs attribute
e=employee()
e.changesalary(12365)
print(e.salary)
print(employee.salary)