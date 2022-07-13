


# class row_colmatrix():
    #  def __init__(self):
    #      self.arr=array
    #      self.target=target



        # IT IS SORTED IN ROW AND COLUMN WISE
def search(matrix,target):
    r=0
    c=len(matrix[0])-1
    while(r<len(matrix) and c>=0):
        if(matrix[r][c]==target):
            return [r,c]
        if(matrix[r][c]>target):
            c-=1
        else:
            r+=1
matrix=[[10,20,30,40],
        [15,25,35,45],
        [28,29,37,49]
        ]

a=search(matrix,49)
# matrix=[[10,20,30,40],
#         [15,25,35,45],
#         [28,29,37,49],
#         [33,34,42,50]]

print(a)
