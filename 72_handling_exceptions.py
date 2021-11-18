try:
    a=int(input("enter the number: "))
    c=1/a
    print(c)
# except Exception as e:
    # print("Exception occured")
    # print(e)
except ValueError as e:
    print("Exception 1 occured ")

except ZeroDivisionError as e:
    print("Exception 2 is occured")

print("thamks for using this code")