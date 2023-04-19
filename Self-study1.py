'''             Casting
If you want to specify the data type of a variable, 
this can be done with casting.'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)

# Get the Type
# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))


""""Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line"""
x = y = z = "Orange"
print(x)
print(y)
print(z)


"""Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. 
This is called unpacking."""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

'''Global Variables
Variables that are created outside of a function (as in all of the examples above)
are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.'''
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

'''If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and 
with the original value.'''

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

'''The global Keyword
Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.'''

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)