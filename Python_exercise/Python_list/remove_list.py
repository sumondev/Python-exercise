thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #1st one is removed but 2nd Banana is still remaining

#Remove Specified Index
#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # it deleted to the last item cherry

#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0] 
print(thislist)

#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # it clear all items but [] empty index is still remaining

