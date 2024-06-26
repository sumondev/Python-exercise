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

#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3,7}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(set1)

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)