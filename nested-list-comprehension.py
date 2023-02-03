# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
res = [num for num in range(1,100) if True in [True for divisor in range(2,10) if num % divisor  == 0 ]]
print(res)

l=[1,2,3,4,5,6]
combi=[(i,j,k) for i in l for j in range(l.index(i)+1,len(l)+1) for k in range(l.index(j)+2,len(l)+1) if i!=j!=k]
print(len(combi))
