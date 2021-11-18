try:
    i=int(input("enter a number: "))
    c=1/i
except Exception as e:
    print(e)
    exit()
finally:                            # when we also exit the programme then also finally runs but 11 line does not run
    print("we are successful")


print("done")