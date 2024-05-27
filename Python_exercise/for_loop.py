# n = int(input("Input a number: "))

# for a in range(n):
#         print(a)

# for a in range(1, n + 1):
#         print(a, end=" ")


# sum =0
# for a in range(0, n+1):
#         sum = sum +a
#         print(sum)


# Assending  Order

# The syntax of the range function is as follows:
# for i in range(start, stop, step):
# For example, if the value of start = 0 and stop = length of the required list and step= 2, then the for loop will iterate over every second element in the entire list

# n = int (input("Input a number"))

# for a in range (0,n+1,2):
     
#         print( a) 

#Decending Order

# n = int(input("Input a number"))
# for a in range(n,-1,-1): 

#     print (a)
    # here 1st n=input number, then it decrese to 0 that;s why write -1, and decase every step -1.

#loop.
# for i in range(1,4):
#     print("\n")
#     for j in range(1,4):
#      print("\n")
#      for k in range(1,4):
#         print(i,j,k)


#Data Structures  tuples
# x = (10,20,30,40,50)
# for var in x:
#     print("index ", str(x.index(var)) , ":",var)
       
       
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)