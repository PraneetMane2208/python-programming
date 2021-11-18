class employee:
    company="yesbank"
    salary=50000
    salarybonus=5000


    @property
    def totalsalary(self):
        return self.salary+self.salarybonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus=val-self.salary

e=employee()
# print(e.totalsalary)
e.totalsalary=70000
print(e.salary)
print(e.salarybonus)