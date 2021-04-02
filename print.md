-BeginPy
# Printing Output in Python

The easiest way for a program to display output to the user is to print out text to the screen. The print function accomplished this by printing whatever is passed to it to the console.

## The How
A print function is called just like any other function, with the name of the function followed by opening and closing parenthesis `print()`. To pass an argument to the function, it is simply placed within the parenthesis.
```py
print("Hello World")

OUTPUT: Hello World
```
This passed argument can be of almost any type, and can be stored in a variable. Multiple arguments can even be passed into one print function.
```py
print(7, "a")
var = ["entry in a list", "entry two"]
print(var)

OUTPUT: 7, a
["entry in a list", "entry two"]
```
If no argument is passed, the print function will default to creating a newline. This means that it moves the output to the next line.
```py
print("part one")
print()
print("part two")

OUTPUT: part one

part two
```

## Communication and Debugging
Displaying output to the screen is useful for two main reasons, firstly as the simplest way for a program to communicate with a user, and secondly as a method of debugging errors.

An example of using the print statement to communicate with the user
```py
x = 5
y = 4
answer = x + y
print(‘The answer is’, answer)

OUTPUT: The answer is 9
```

Creating a graphical user interface, or gui, is not needed for many applications, and would grow a relatively small project in to a much larger one if it was included. For this reason command line based applications are not only accepted, but encouraged unless a gui is truly needed. 