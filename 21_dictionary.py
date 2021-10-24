# mydict = { "praneet" : "batsman",
        #   "marks" :[25,65],
        #  "fast" : "jaldi",
#   "anotherdict" : {'praneet' : 'bowler'}




# print(mydict['fast'])
# print(mydict["praneet"])
# mydict = { "praneet" : "batsman",
# print(mydict['anotherdict']['praneet'])
mydict = { "praneet" : "batsman",
          "marks" :[25,65],
         "fast" : "jaldi",
  "anotherdict" : {'praneet' : 'bowler'}
}
# print(mydict.values())
# print(mydict.items())
# print(list(mydict.keys()))
# print(mydict)   

updatedict = { "hero" : "power" ,
    "scotland" : "country"              #updates the keys and values in my dict  


}

# mydict.update(updatedict)
# print(mydict["praneet1"])    # it throws an error
print(mydict.get("praneet1"))   # it shows none it means that this value is not present in my dict    *imp interview question