#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#With list comprehension you can do all that with only one line of code:
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#copy all item new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)