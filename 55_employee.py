class employee:
    company="google"
    salary=2000

praneet=employee()
pavan=employee()
praneet.salary=50000
pavan.salary=90000
print(praneet.company)
print(pavan.company)
employee.company="morgan stanley"
print(praneet.company)
print(pavan.company)
print(pavan.salary)