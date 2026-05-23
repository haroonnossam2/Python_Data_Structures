# Find Second Largest Element
'''a = [3,6,2,10]
a.sort()
print(a[-2])'''

#  Remove Duplicates from List
'''nums = [1, 2, 2, 3, 4, 4, 5]
j=[]
for i in nums:
    
    if i not in j:
        j.append(i)
    
print(j)'''

#Reverse a List
'''nums = [1, 2, 3, 4]
nums.sort(reverse=True)
print(nums)'''

# Find Even Numbers from List
'''nums = [1, 2, 3, 4, 5, 6]
y= [x for x in nums if x%2==0]
print(y)'''

# Find Sum of All Elements
'''nums = [1, 2, 3, 4]
j=0
for i in nums:
    j+=i
print(j)'''
#Find Common Elements Between Two Lists
'''a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)'''

# Find Frequency of Elements
'''nums = [1, 2, 2, 3, 3, 3]
c={}
for i in nums:
    if i in c:
        c[i]+=1
    else:
        c[i] = 1
print(c)'''

#Flatten Nested List
'''a = [1, 2, [3, 4], [5, [6, 7]]]
c=[]
def nest(b):
    for i in b:
        if type(i)==list:
            nest(i)
        else:
            c.append(i)
nest(a)
print(c)'''

#Left Rotation
'''nums = [1, 2, 3, 4, 5]
k = 2
rotated = nums[k:] + nums[:k]
print(rotated)'''

#Check List is Palindrome
'''nums = [1, 2, 3, 2, 1]
if nums == nums[::-1]:
    print("Palindrome")
else:
    print("No palindrome")'''


#missing nuber
"""nums = [1, 2, 3, 5]

n = 5

missing = n*(n+1)//2 - sum(nums)

print(missing)"""

#Prefix Sum
'''nums = [1, 2, 3, 4]
c=[]
j=0

for i in nums:
    j+=i
    c.append(j)
print(c)

#outpu: [1, 3, 6, 10]'''