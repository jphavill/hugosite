# Using If Else Logic 

An if else statement is what allows a program to respond in real time to outside input. With these statements, the program can change what code is executed based on variables within the program.

---

## Why If Else Statements are Used
Without if else statements every program would run identically every time,  severely restricting its usefulness. It is these statements which allow a calculator to deal with dividing by zero, a website to validate login credentials, and a game to discover when a shot has landed.

---

## Structure of If Else
```py
number_A = 5
number_B = 4
if number_A > number_B:
```
The statement begins with the `if` keyword, followed by the condition, then a colon, and finally an indented block of code. This code will only run if the condition is true.
```py
number_A = 5
number_B = 4
if number_A > number_B:
  print("number A is bigger than number B")

OUTPUT: number A is bigger than number B
```
 In the examples above the code runs just fine without the final part of an if else statements, the else. Here the program will simply skip over the indented code if the conditional is false, and continue on. However, in many cases it is useful to have a dedicated section of code to run if the condition is false, and this is done with the `else`  keyword. It is used in the same way as the `if` keyword,  with a  colon following it and then its own indented block of code.
```py
number_A = 2
number_B = 4
if number_A > number_B:
  print("number A is bigger than number B")
else:
  print("number B is bigger than number A")

OUTPUT: number B is bigger than number A
```

A computer treats an if else statement as a branch in the rails of your program, with the conditional acting as the switch. After either the indented code under either the  `if`  keyword or the  `else`  keyword has been run, the code continues on in its normal linear fashion.
```py
print("program begins")
number_C = 2
number_D = 4

if number_C > number_D:
  print("number C is bigger than number B")
else:
  print("number D is bigger than number A")

print("program continuing to run")

OUTPUT: program begins
number B is bigger than number A
program continuing to run
```
---

## Practical Uses of If Else
If the guesses number is correct
```python
print("Please attempt to guess the number between 1 and 10")

magic_number = 6

guess = int(input("What is your guess"))

if guess < magic_number:
  print("To low")

```

---

## Practice Problems
