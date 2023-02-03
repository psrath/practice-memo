import functools as ft
import numpy
##Approach-1
lst = [2,4,5,6]
print(ft.reduce(lambda x,y:x+y,lst))
##Aproach-2
s=0
for i in lst:s+=i
print(s)
print(numpy.sum(lst))
print(numpy.max(lst))
