class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getstatus(self):
        print(f"the name of the train is {self.name}")
        
        print(f"the seats in the train is {self.seats}")


    def fareinfo(self):
        print(f"the fare of the train is {self.fare}")

    def bookticket(self):
        if (self.seats>0):
            print(f"your seat is booked and your  seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry train is full")
    def cancelticket(self):
        self.seats=self.seats+1

a=train("kalyan express",10000,100)
a.bookticket()
a.bookticket()
a.bookticket()
a.fareinfo()
a.getstatus()
a.cancelticket()