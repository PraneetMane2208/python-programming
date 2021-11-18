class c2dvec:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def __str__(self):
        return f"{self.i}i + {self.j}j"

class c3dvec(c2dvec):
    def __init__(self,i,j,k):
        super().__init__(i, j)
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j+{self.k}k"

v2d = c2dvec(1,5)
v3d = c3dvec(7)
print(v2d)
print(v3d)
