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

print("Increment the sequence with 3 (default is 1):")
for x in range(2, 30, 3):
  print(x)  

print("Print all numbers from 0 to 5, and print a message when the loop has ended:g")
for x in range(6):
      print(x)
else:
  print("Finally finished!")

print("If the loop breaks, the else block is not executed.")
for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Finally finished!")