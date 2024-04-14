#############We are learning Python List###################

# this_list= ["apple","banana","mango"]

# print(this_list)
# print(len(this_list))
# print(type(this_list))

######################Access list item#####################
# my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(this_list[1])  # it allow just only one element
# print(my_list[2:5]) # it allows the range of starting and before ending element

# print (my_list [:3]) # it allows 0 inedxt to before 3. that means 0 to 2
# print (my_list[3:]) # it allows 3 index to end endex

################check for if item exists###################

# if "apple" in my_list:
#     print ("yes, apple is in this list")

########### Change List item Value #################

# my_list[1]= "graphes"
# print(my_list)  # here banana is changed over graphes as array 1 podition

# my_list[0:2] = ["lichi","coconut"] # it changed the array position 0 and 1. 
# print(my_list)

# my_list[0:1]=["papya","plam","guava"] # it will add 3 new items replacing by lichi before arrary no 1. 
# print(my_list)
# print(len(my_list))

# my_list[1:10]= ["white apple"] # it replaced all item 1 to 1o .
# print(my_list)



##############Insert Item ####################

# my_list = ["apple", "banana", "cherry"]
# my_list.append("orange")   #append is used for add  value last of arrary
# print(my_list)

# my_list.insert(1, "lichi") # now lichi will be inserted array no 1
# print(my_list)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)
# print(thislist)

##########Add elements of a tuple to a list##########
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

###### Remove List ##########
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

######## Remove Specified Index ##########
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

####### if pop method is not specified then it remove last element
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist) 


# ##### the del keyward aslo used for remove specified item ##########
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# ########## delete the entire list #########
# thislist = ["apple", "banana", "cherry"]
# del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
