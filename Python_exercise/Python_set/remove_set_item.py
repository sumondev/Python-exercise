#To remove an item in a set, use the remove(), or the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#the del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)