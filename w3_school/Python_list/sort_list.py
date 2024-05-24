
#Sort List Alphabatically Acsending Order
thislist = ["apple", "banana", "cherry", "mango", "kiwi"]
thislist.sort()
print(thislist)

thislist=[100,40,50,80,70]
thislist.sort()
print(thislist)

#Sort Descending Order
thislist = ["apple", "banana", "cherry", "mango", "kiwi"]
thislist.sort(reverse=True)
print(thislist)

thislist=[100,40,50,80,70]
thislist.sort(reverse=True)
print(thislist)


#Customize sort function by using keyword argument key = function, the function will return a number that will be used to sort the list. (the lower number 1st)
#Example1. Sort the list based on how close the  number is close to 50.

def myfunc(n):
    return abs(n-100)

thislist = [40,50,90,10,500,200]
thislist.sort(key = myfunc)
print(thislist)


#case sensitive sorting give unexpected result
#That why we use str.lower or upper to fix tgis problem.
thislist = ["apple", "Banana",  "Mango","cherry", "kiwi"]
thislist.sort(key=str.lower)
print(thislist)


thislist = ["apple", "banana", "cherry", "mango", "kiwi","orange","pineapple"]
thislist.reverse()
print(thislist)

