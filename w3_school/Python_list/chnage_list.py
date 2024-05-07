# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# #copy this one another variable with slicing technique
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# newlist = thislist[:]  # Copy the list using slicing
# print(newlist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

#Insert a new value
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist.insert(3, "orange")
print(thislist)

#Using list concatenation and slicing:
thislist = ["apple", "banana", "cherry"]
values_to_insert = ["watermelon", "orange"]
thislist = thislist[:2] + values_to_insert + thislist[2:]
print(thislist)



