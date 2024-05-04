#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age
# print(txt) 


#But we can combine strings and numbers by using f-strings or the format() method!

#Ex-1
age = 28
txt =f" My name is Sumon, I am {age}"
print(txt)

#Ex-2
#Placeholders and Modifiers , A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 50
txt =f"The price is {price*2}"
print(txt)

#Ex-3
#A modifier is included by adding a colon : followed by a legal formatting type, like .3f which means fixed point number with 2 decimals:
price = 50
txt =f"The price is {price*2:.3f}"
print(txt)