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

