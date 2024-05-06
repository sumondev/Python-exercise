#1 Here we are using python slicing from string
v1 = "hello-python"
print(v1[1:6])  # it printed from element 1 to 5, slicing at the range
print (v1[:6]) # it printed from begining of element to before 6, Slice From the Start
print(v1[0:]) #it  printed from 0 to last of the element, Slice to the end
print(v1[-1:0]) # it slicing last to frist but in acending order.
print(v1[0:-1]) # it slicng 0 to before last element
print(v1[-1:-5]) # it slicing is also not be executed
print(v1[-5:-1]) # this slicing also empty because of range is not in order 
print(v1[-5:1]) # this kind of slicing have empty because of range is over boundary
#here all are exapmle is string slicing.

#Another Example
# Define a string
my_string = "Hello, World!"
# Extracting a substring using slicing
substring1 = my_string[0:5]  # Starting from index 0 (inclusive) to index 5 (exclusive)
substring2 = my_string[7:]   # Starting from index 7 (inclusive) to the end of the string
substring3 = my_string[:5]   # Starting from the beginning to index 5 (exclusive)
substring4 = my_string[::2]  # Starting from the beginning to the end, with a step of 2

# Print the results
print("Original String:", my_string)
print("Substring 1:", substring1)  # Output: "Hello"
print("Substring 2:", substring2)  # Output: "World!"
print("Substring 3:", substring3)  # Output: "Hello"
print("Substring 4:", substring4)  # Output: "Hlo ol!"

