#Python List Methods
# 1. append()
# Adds a single element to the end of the list.
n = [2,4,56]

while True:
    m= int(input("enter number"))
    if m==0:
        break
    else:
        n.append(m)
print(n)

#  examp
a = [1,2,3,[3,5,46,[4,7,8,3]]]
m= []
def exten(n):
    for i in n:
        if type(i)==list:
            exten(i)
        else:
            m.append(i)
exten(a)
print(m)

Outpit:-[1, 2, 3, 3, 5, 46, 4, 7, 8, 3]

# 2. extend()
# Adds multiple elements from another iterable.
nums = [1, 2]
nums.extend([3, 4])

print(nums)
# [1, 2, 3, 4]

3. insert()
Inserts an element at a specific position.
nums = [1, 3]
nums.insert(1, 2)

print(nums)
# [1, 2, 3]
Syntax:
list.insert(index, value)


4. remove()
Removes the first occurrence of a value.
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)
# [1, 3, 2]


5. pop()
Removes and returns an element.
nums = [1, 2, 3]
x = nums.pop()
print(x)
# 3
print(nums)
# [1, 2]

Using index:
nums.pop(0)

6. clear()
Removes all elements from the list.
nums = [1, 2, 3]
nums.clear()
print(nums)
# []

7. index()
Returns index of the first matching value.
nums = [10, 20, 30]
print(nums.index(20))
# 1

8. count()
Returns how many times an element appears.
nums = [1, 2, 2, 3]
print(nums.count(2))
# 2

9. sort()
Sorts the list in ascending order.
nums = [4, 1, 3, 2]
nums.sort()
print(nums)
# [1, 2, 3, 4]

Descending order:
nums.sort(reverse=True)

10. reverse()
Reverses the list.
nums = [1, 2, 3]
nums.reverse()
print(nums)
# [3, 2, 1]

11. copy()
Creates a shallow copy of the list.
nums = [1, 2, 3]
new_nums = nums.copy()
print(new_nums)
# [1, 2, 3]

Useful Built-in Functions Used with Lists
len()
Returns length of list.
\nums = [1, 2, 3]
print(len(nums))
# 3

max()
Returns largest element.
print(max([1, 5, 3]))
# 5

min()
Returns smallest element.
print(min([1, 5, 3]))
# 1

sum()
Returns total sum.
print(sum([1, 2, 3]))
# 6

sorted()
Returns a new sorted list.
nums = [3, 1, 2]
print(sorted(nums))
# [1, 2, 3]

List Operators
Concatenation (+)
a = [1, 2]
b = [3, 4]
print(a + b)
# [1, 2, 3, 4]

Repetition (*)
print([1, 2] * 3)
# [1, 2, 1, 2, 1, 2]

List Slicing
nums = [0, 1, 2, 3, 4]
print(nums[1:4])
# [1, 2, 3]

List Comprehension
squares = [x for x in range(20) if x%2==0]
print(squares)
# [0, 2, 4, 8, 10]


