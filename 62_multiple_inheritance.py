class employee:
    company="phonpe"
    ecode=456

class freelancer:
    company="fiver"
    level=0

    def upgradelevel(self):
        self.level=self.level+1

class programmer(employee,freelancer): #whichever class is written first in bracket after print it executes that
    name="pavan"

p=programmer()
p.upgradelevel()
print(p.company)