def my_function():
  print("Hello from a function")

#Calling a Function  
def my_function():
      print("Hello from a function")
my_function()

#Arguments
def my_function(fname):
      print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Emil", "Refsnes")

#This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
      print(fname + " " + lname)
my_function("Emil")
#it will be get an error