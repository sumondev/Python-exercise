# Here we are learing Python-modifu Strings
#Upper Case
v1= "Hello,Python"
print(v1.upper())
print(v1.lower())

v1= "    Hello Python   "
print(v1.strip()) # it removes white space from the begin and end.

#String replace
v1 = "Hello,Python"
print(v1.replace("H","W")) # it replaces H to W.

v1= "Hello, Python"
print(v1.replace("Hello,","Hi"))

v1= "Hello,Python,welcome"
print(v1.split(",")) # The split() method splits the string into substrings if it finds instances of the separator