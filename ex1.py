# x,y,z = "Sumon",5.25,7
# message=  f"My name is {x} \n, My point is {y}, and my roll is {z}"
# print(message)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# python list example

# list = ["apple", "banana", "cherry"]
# print(list)
# print(len(list)) #len is used for count list item

#It also possibe to use list constractor to use list

# my_list=list(("apple","banana","cherry"))
# print(my_list)

# print(my_list[2],my_list[0]) # is also assign the value by index number

# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(this_list[2:5])  #it is used for range 
# print(this_list[:4]) # it begins from 0 to 4 but inlude only 0 index to 3 index value. 
# print (this_list[1:]) # it begins from given (1) index to end index value


# if "orange" in this_list:
#   print("Yes, 'orange' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

#################List Comprehension#########
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# newlist = [x for x in range(10)]
# print(newlist)
# newlist = [x for x in range(10) if x < 5]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x.upper() for x in fruits]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "banana", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

############# Sort ############

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

############3 Decending #########
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)