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

print("continue statement in for loop") 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  #here banana is skiped 
print("Range loop")
for x in range(6):
  print(x) 

print("using start perameter")
for x in range(2, 6):
  print(x)  