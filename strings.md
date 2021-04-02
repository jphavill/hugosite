-BeginPy
# Working with Strings in Python

A string is a data type that stores a series (or "string") of characters. These characters could make up a word, a sentence, or even entire paragraphs. 

---

## The How

A string is denoted by surrounding characters in either single `'` or double `"` quotes.

```py
myString = "This is a string denoted with double quotes"
myOtherString = 'This is also a string, instead denoted with single quotes'
```
The variable name can then be used in place of the string.

```py
myString = "This is a string denoted with double quotes"
print(myString)

OUTPUT: This is a string denoted with double quotes
```

### Indexes

Individual characters of a string can also be accessed using the position, or index, of the character in the string.

```py
myString = "ABCD123!"
print(myString[2])

OUTPUT: C
```
You may have noticed that even though index 2 was used, the third character was printed. This is because strings are indexed starting at 0. Here are some more examples.

```py
myString = "ABCD123!"
print(myString[0])
print(myString[1])

OUTPUT: A
B
```

### Slices

Sections of a string can also be accessed. This is done using a format called slicing. The start and end index of the section you want to "slice" out of the string is separated by a colon and placed in square brackets after the string or variable.

```py
scene = "01opening"
scene_number = scene[0:2]
print(scene_number)

OUTPUT: 01
```

Just like tuples and lists, the character at the position of the first number is included, while the character at the position of the second number is not.

---

## The Why
Strings are used to store any type of data that isn't numerical in nature. Without strings text based data would have to be stored using ascii codes, or some other numerical conversion of characters which drastically reduces the readability to human coders.
---

## Practical Uses
Strings can be used to store filenames, usernames, passwords.
---

## Extras

---

### extra1

