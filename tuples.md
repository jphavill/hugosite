# Storing Data in Tuples

A tuple is a data type which stores other data types in an ordered index. For example, a tuple can store integers, floats, strings, and even other tuples. You cannot add to or remove data from a tuple once it has been created.

---

## Creating a Tuple
Just as a string is denoted by surrounding characters in quotes

```py
my_string = "some text"
```

Tuples are created by surrounding data in round brackets.

```py
my_tuple = (my_string, 5, "message", 4.7)
```

To access this stored data, the position of the data, or index, is used. This is done by placing the index in square brackets following the name of the tuple.

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)
print(my_tuple[1])

OUTPUT: 5
```

You may have noticed that even though index 1 was used, the second piece of data was printed. This is because tuples are indexed starting at 0. Here are some more examples to help you understand.

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)
print(my_tuple[0])

OUTPUT: some text
```

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)
print(my_tuple[3])

OUTPUT: 4.7
```

A negative number can also be used for the index of a tuple. In that case, the last item of a tuple is denoted by -1, and the index works backwards from there.

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)
print(my_tuple[-1])

OUTPUT: 4.7
```

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)
print(my_tuple[-3])

OUTPUT: 5
```

Finally, data in a tuple can be accessed in slices in the same way as a string. This is done by indicating the starting item and the ending item, which will not be included. Theses values are separated by a colon and placed within square brackets.

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)
print(my_tuple[1:3])

OUTPUT: (5, "message")
```

Tuples can also be iterated over using a for loop in the same way as a range.

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)

for I in my_tuple:
  print(i)

OUTPUT: some text
5
message
4.7
```
Finally, tuples can be used in logic expressions to check if a piece of data is in the tuple, or at a specific index in the tuple.

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)

if "message" in my_tuple:
  print(True)

OUTPUT: True
```

```py
my_string = "some text"
my_tuple = (my_string, 5, "message", 4.7)

if my_tuple[0] == "message":
  print(True)

OUTPUT: True
```
---

## The Why
A tuple offers an easier way to store large amounts of related data, especially when a similar action needs to done to that data. For example, storing sets of x, y, z coordinates in a tuple makes sense, as they are only useful as a set.

An example of data that is closely related.

```py
position_one = (3, 2, 5)
position_two = (2, 4, 7)

Delta_X = position_one[0] - position_two[0]
print(Delta_X)

OUTPUT: 1
```

An example of data that is iterated over.

```py
code = ("red", "green", "blue", "yellow")
guess = ("red", "black", "yellow", "green")
counter = 0
red_count = 0
white_count = 0

for colour in guess:
  if colour == code[counter]:
    red_count += 1
  elif colour in code:
    white_count += 1
  counter += 1

print("Red", red_count, "White", white_count)

OUTPUT: Red 1 White 2
```
---

## Practical Uses
A common practice when asking the user for input is to give them a few options to choose from. When combined with a while loop tuples allow a program to easily test if the input is one of the available options.

```py
choice = 0
options = ("y", "n", "q")
while choice not in options:
  choice = input("Choose an option", options)
  print("Your choice was", choice)

OUTPUT: Choose an option ("y", "n", "q")
USERINPUT: l
OUTPUT:	Choose an option ("y", "n", "q")
USERINPUT: y
OUTPUT:	Your choice was y
```

Another practical use of tuples, as shown above, is to organize related data and iterate over it. In this example, the program finds the first positive number divisible by the numbers (2, 3, 7). By writing the program using a tuple, it is easy to change the requirements, as they are all organized under one variable.

```py
divisors = (2, 3, 7)
number = 2
divisibility = False

while divisibility is False:
  divisibility = True
  for i in divisors:
    if number % i != 0:
      divisibility = False
        break
  number += 1

print(number)

OUTPUT: 43
```
---

## Practice Problem
Your problem is to take two coordinates and calculate the equation of the line they make.

HINT: a line can be represented by the equation y - y1 = m * (x-x1) where m represents the slope and y1 and x1 represent the values of a point on a line.

```py
coor_one = (4, 7)
coor_two = (2, 12)
```

You must then find which of the following points fall on that line and print them out.

```py
points = ((2, 12), (3, 13), (4, 7), (6, 2), (7, -3), (10, -8), (16, -23.0))
```

HINT: When you use the index of a tuple to return a value, it will return whatever is at that position, even another tuple. If you’re still stuck, look at nested tuples in Extras.

This is a sample solution, you can reveal it with the button below.

```py
coor_one = (4, 7)
coor_two = (2, 12)

points = ((2, 12), (3, 13), (4, 7), (6, 2), (7, -3), (10, -8), (16, -23.0))

m = (coor_two[1] - coor_one[1]) / (coor_two[0] - coor_one[0])
print("y -", coor_one[1], "=", m, "* ( x -", coor_one[0], ")")

for point in points:
  if -2.5*(point[0]-4) + 7 == point[1]:
    print("The point", point, "is on the line.")
```
---

## Extras

### Nested Tuples:
Tuples can store most other data types, including other tuples. This is done exactly as you would expect, with the syntax

```py
nested_tuples = (("tuple1", 1), ("tuple2", 2))

new_tuple = nested_tuples[0])

print(new_tuple)

OUTPUT: ("tuple1", 1)
```

As you can see, this returns the tuple. If we wanted to get the second value of this nested tuple, we would use the syntax

```py
print(new_tuple[1])

OUTPUT: 1
```

This two-step process can be combined into a new syntax

```py
print(nested_tuples[0][1])

OUTPUT: 1
```

First, `nested_tuples[0]` returns the tuple `("tuple1", 1)`.  Next, we get the value at index 1 of this new tuple, returning 1.

### Nested Tuple Iteration:
You can also iterate over the value in nested tuples, though they must all have the same number of items. This is done by assigning a variable to each index of the nested tuples using the syntax

```py
nested_tuples = (("tuple1", 1), ("tuple2", 2))

for name, number in nested_tuples:
  print(name)
  print(number)

OUTPUT: tuple1
1
tuple2
2
```

### Enumerate:
The `enumerate()` function is useful when you need to iterate through both the items of a tuple and their position within the tuple. The function adds the index of each item to a tuple with each item, making a tuple of tuples and allowing you to iterate through with a counter variable and a variable assigned to the original items.

Bonus: the `tuple()` function returns a tuple of the value passed to it, such as `range()`, value separated by commas, or the `enumerate()` function.

```py
my_tuple = ("a", "b", "c")
print(tuple(enumerate(my_tuple)))

OUTPUT: ((0, "a"), (1, "b"), (2, "c"))
```

```py
for counter, item in enumerate(my_tuple):
  print(counter)
  print(item)

OUTPUT:	0
a
1
b
2
```
