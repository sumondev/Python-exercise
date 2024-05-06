# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

#copy this one another variable with slicing technique
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
newlist = thislist[:]  # Copy the list using slicing
print(newlist)


