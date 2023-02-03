#Find all the number form [1-100] that are divisiable by 8
res = [items for items in range(1,100) if not items%8]
print(res)
#Find all of the numbers from 1–1000 that have a 6 in them
r2 = [items for items in range(1,100) if  items%10==6]
print(r2)
#Count the number of space in a string
r3 = [items for items in 'Practice Problems to Drill List Comprehension in Your Head.'.split(' ')]
print('Space in the string '+str(len(r3)-1))
#Remove all of the vowels in a string (use string above)
r4 =[ch for ch in 'Practice Problems to Drill List Comprehension in Your Head.' if ch not in ['a','e','i','o','u']]
print(*r4)
#Find all of the words in a string that are less than 5 letters (use string above)
r5 = [items for items in 'Practice Problems to Drill List Comprehension in Your Head'.split() if len(items)<5 ]
print(r5)
#Use a dictionary comprehension to count the length of each word in a sentence (use string above)
r6 = {items:len(items) for items in 'Practice Problems to Drill List Comprehension in Your Head'.split()}
print(r6)

# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
res = [num for num in range(1,100) if True in [True for divisor in range(2,10) if num % divisor  == 0 ]]
print(res)

##
