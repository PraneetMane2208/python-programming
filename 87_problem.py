name =input("enter your name  : ")
marks= input("enter your marks : ")
phone =input("enter your number : ")

template="the name of the student is {}, his marks are {},and his phone number is {} "
output=template.format(name,marks,phone)
print(output)