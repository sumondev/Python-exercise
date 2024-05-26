thisset = {"apple", "banana", "cherry"}

print(thisset)

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Trur and 1 is considered to same value
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered to same value

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


#get an no of this item
thisset = {"apple", "banana", "cherry"}

print(len(thisset))