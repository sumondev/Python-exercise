thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year" : 1994

}
x = thisdict["model"]
print (x)

#There is also a method called get() that will give you the same result:
x = thisdict.get("year")
print(x)

x = thisdict.keys()
print(x)
#it shows all key of the dictionary

