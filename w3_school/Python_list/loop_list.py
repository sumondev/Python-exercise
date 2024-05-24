#Print all items in the list, one by one:

this_list=["x","y","z"]
for x in this_list:
    print(x, end = "") # one line print
print("\n")
#we can also  loop through the list items by referring to their index number.
print("Using for loop")
this_list=["x","y","z"]
for i in range(len(this_list)):
    print(i)
print("\n")


print("Using While loop")
this_list = ["apple", "banana", "cherry"]
i=0
while(i<len(this_list)):
    print(i)
    i=i+1
print("\n")


print("Looping Using List Comprehension \nA short hand for loop that will print all items in a list:")
thislist = ["apple", "banana", "cherry","Banana"]
[print(x) for x in thislist]