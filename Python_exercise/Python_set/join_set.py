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
print(myset)