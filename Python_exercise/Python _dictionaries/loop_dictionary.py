#Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#   for x in thisdict.keys():
#       print(x) # we can use this method for use to print key values

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
# for x in thisdict.values():
#   print(x) # we can also use this method


#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)