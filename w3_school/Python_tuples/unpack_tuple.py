#packing a tuple like that.
fruits = ("apple", "banana", "cherry")
print(fruits)

#Now we are learning how to unpack a tuple
 
fruits = ("apple", "banana", "cherry")
(green,yellow,red)=fruits #now every values is unpacked with variable
print(green,yellow,red)

#Using Asterisk* If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red) # but this red valu store value as a list.

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "cherry", "strawberry", "raspberry", "banana")
(green,*red,yellow)=fruits
print(green)
print(red)
print(yellow)
