#The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a","b","c"}
y = {1,2,3}
z=x.union(y)
print(z)

x = {"a","b","c"}
y = {1,2,3}
z=x|y
print(z)
#the | operator is also same as join operator

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

myset= set1 | set2 |set3 |set4
print(myset)\


#Join a Set and a Tuple
#The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.



#The update() method inserts all items from one set into another. The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,3}

set1.update(set2)
print(set1)
#Note: Both union() and update() will exclude any duplicate items.


#You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)


#The difference() method will return a new set that will contain only the items from the first set that are not present in the other se
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.difference(set2)
print(set3)
#we can use - oprator for geting the same result

set4 = set1-set2
print(set4)

#diiference_update is also same but it store the value of begening set which is started first.
set1.difference_update(set2)
print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.symmetric_difference(set2)
print(set3)

#we can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set4 = set1 ^ set2
print(set4)

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1.symmetric_difference_update(set2)

print(set1)