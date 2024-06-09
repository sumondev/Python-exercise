fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Loop through the latters
print("loop in letters")
for x in "banana":
  print(x)  


print("Exit the loop when x is Banana:")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break 


print("Exit the loop when x is banana, but this time the break comes before the print:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 