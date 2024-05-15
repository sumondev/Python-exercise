#To add an item to the end of the list, use the append() method:

f_list=["Banana","Apple","Coconut"]
f_list.append("Orange")
print(f_list)

#To insert a list item at a specified index, use the insert() method.
f_list=["Apple","coconut"]
f_list.insert(1,"Mangoes")

f_list.insert(2,"Coconut")
print(f_list)

#To append elements from another list to the current list, use the extend() method.
f_list1 = ["mangoes","Banana","lichi"]
f_list2 = ["coconut","pineapple","Orange"]
f_list1.extend(f_list2)
print(f_list1)

#Add elements of a tuple to a list:

f_list1 = ["mangoes","Banana","lichi"]
f_touple1 = ("Guava","Lemon")
f_list1.extend(f_touple1)
print(f_list1)


