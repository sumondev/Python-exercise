# Task 1.
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If  n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n  is even and greater than 20 , print Not Weird

# if __name__ == '__main__':
#     n = int(input().strip())

# if n%2 != 0:
#     print("Weird")
# else:
#     if n>=2 and n<=5:
#         print("Not Weird")
#     elif n>=6 and n<=20:
#         print("Weird")
#     elif n>20:
#         print("Not Weird")


# Task 2.
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a-b)
#     print(a*b)


# Task 3
# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,a  //b. 
# The second line should contain the result of float division, a /b .

# No rounding or formatting is necessary.

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print( int (a/b))
#     print(float (a/b))


# Task 4
# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, printi^2 .
# Example
# The list of non-negative integers that are less than 3 is [0,1,2] . Print the square of each number on a separate line. 

# if __name__ == '__main__':
# n = int(input())
# for i in range(n):
#      print(i**2)


# Task: 5
# Write a function

# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary, day and we add it to the shortest
# month of the year, February. 
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.

# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT
# leap years.

# Task 6
# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.

# Input Format
# Read y, the year that needs to be checked.

# Constraints
# 1900 <= y <= 10**5

# Output Format
# Output is taken care of by the template. Your function must return a boolean value (True/False)

# def is_leap(year):
#     leap = False
    
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
    
#     return leap

# year = int(input())
# print(is_leap(year))

# task.7
# The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following: 123……..n

# Note that "..." represents the consecutive values in between.

# Example
# n = 5

# Print the string 12345 .


# if __name__ == '__main__':
#     n = int(input())
   
#     for x in range(n):
#         x+=1
#         print(x, end="")

       
#     if __name__ == '__main__':
#         n = int(input())
#     y = range (1, n+1)
#     for x in y:
#         print(x, end='')
       