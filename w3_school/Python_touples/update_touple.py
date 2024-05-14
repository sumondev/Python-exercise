
# AS we know tuple si unchagable , so we can not add, change or remove it. to do that we can convert it in list then after operation we can easily conver it list to touple again.

x = ("a","b","c") #this is touple
y = list(x) # touple is converted to list
print(y)
y[1]= "b1" # change element 1 , from b to b1
print(y)
c =tuple(y) # Converted to tuple again
print(c)