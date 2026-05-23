'''A Tuple is:

Ordered
Immutable (cannot change)
Allows duplicate values
Written using ()

Difference Between List and Tuple
Feature	List	Tuple
Syntax	[]	()
Mutable	Yes	No
Methods	Many	Only 2
Performance	Slower	Faster
Memory	More	Less
When to Use Tuple

Use tuples when:

Data should not change
Faster performance needed
Fixed values required
Used as dictionary keys'''

Example:

coordinates = (12.5, 45.8)
Example:

t = (1, 2, 3)
Creating Tuples
Normal Tuple
t = (1, 2, 3)

print(t)
Single Element Tuple

Comma is mandatory.

t = (5,)

print(type(t))
Without Parentheses
t = 1, 2, 3

print(t)
Accessing Tuple Elements
Indexing
t = (10, 20, 30)

print(t[0])
print(t[2])
Negative Indexing
print(t[-1])
Tuple Slicing
t = (1, 2, 3, 4, 5)

print(t[1:4])

Output:
(2, 3, 4)
Tuple Methods

Tuples have only 2 methods.

1. count()

Counts occurrences.

t = (1, 2, 2, 3)

print(t.count(2))

Output:
2

2. index()

Returns first index of value.

t = (10, 20, 30)

print(t.index(20))

Output:

1
Tuple Packing
t = 1, 2, 3

print(t)
Tuple Unpacking
a, b, c = (10, 20, 30)

print(a)
print(b)
print(c)
Nested Tuple
t = ((1, 2), (3, 4))

print(t[1][0])

Output:

3
Convert List to Tuple
l = [1, 2, 3]

t = tuple(l)

print(t)
Convert Tuple to List
t = (1, 2, 3)

l = list(t)

print(l)
Tuple Operators
Concatenation (+)
a = (1, 2)
b = (3, 4)

print(a + b)
Repetition (*)
print((1, 2) * 3)

Output:
(1, 2, 1, 2, 1, 2)

Built-in Functions with Tuple
len()
t = (1, 2, 3)

print(len(t))
max()
print(max((4, 7, 2)))
min()
print(min((4, 7, 2)))
sum()
print(sum((1, 2, 3)))
