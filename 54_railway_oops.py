class railwayform:
    formtype="railway form"
    def printdata(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

praneetsapplication=railwayform()
praneetsapplication.name="praneet"
praneetsapplication.train="rajdhani express"
praneetsapplication.printdata()