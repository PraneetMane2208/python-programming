a = '''Dear <|name|>,
you are selected for interview
date :<|date|>'''
name = input("enter your name : ")
date = input ("enter date :")

print(a.replace("<|name>|",name))
# a = a.replace("<|name|>",name)
# a = a.replace("<|date|>", date)      #imp notes
print(a)