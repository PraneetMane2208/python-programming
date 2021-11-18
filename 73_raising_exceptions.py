def increement(num):
    try:
        return int(num)+1
    except:
        raise ValueError("it is incorrect")

a=increement('gffffue')
print(a)