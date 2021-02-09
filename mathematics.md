# Integer Math in Python

A core part of any programming language is it's ability to compute mathematical problems, from processing data sets to calculating what pixels to display on a screen. Just as in traditional mathematics, these problems can be broken down and expressed as smaller operations. These include simple operations, such as addition and multiplication, and a few of the more exotic functions like sin and cosine. 

---

## arithmetic operations
1. addition `1 + 2`
2. subtraction `2 - 1`
3. multiplication `2 * 3`
4. division `4 // 2`
5. modulo `16 % 3`

In python these evaluate to their answers in place. For example, assigning a variable to the value `3 * 2` would give it the value of 6.

```python
myNumber = 3 * 2

print(myNumber)

OUTPUT: 6
```

---

## The Why
From calculating the position of an enemy in a video game, to determining how wide the window of an application should be, to simply coding a calculator, almost all programs will use math in one way or a another.
---

## Practical Uses
One of the most common uses for math in a program is to count how many times something has happened using basic addition. 

```python
count = 0
while count < 3:
    count = count + 1
    print("this loop has run", count, "times so far.")


```
---

## Practice Problem
Your problem is to take a variable starting at 1, and change it to each of the following numbers 1, 66, 42, 49, 7 and 0 in that order, using each arithmetic operator at most one time. An example of the correct output would be

```python
OUTPUT: 1
66
42
49
7
0
```

This is a sample solution, you can reveal it with the button below.

```python
number = 1
print(number)
number = number * 66
print(number)
number = number - 24
print(number)
number = number + 7
print(number)
number = number // 7
print(number)
number = number % 7
print(number)
```
---

## Extras

### Inline Operators
If you want to change the value of a variable, there is a shortcut syntax for writing mathematical operators. Instead of writing `num = num + 1` you can instead write `num += 1`. This can be done for any of the arithmetic operators listed above.

