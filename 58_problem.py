class programmer:
    company="microsoft"
    # def __init__(self,name,subunit):
        # self.name=name
        # self.subunit=subunit

    def getinfo(self):
        print(f"the name of programmer is {self.name}  and the name of subunit is{self.subunit}")


praneet=programmer("praneet","crazymonk")
pavan=programmer("pavan","gslab")
praneet.getinfo()
pavan.getinfo()