def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this = "  praneet   is bad boy"
n= remove_and_strip(this, "praneet")
print(n)