import functools as ft
l=[1,3,4,5,6,8,12,13,14,15,20]
even=[items for items in l if not items%2]
odd=[items for items in l if items%2!=0]
print(even)
print(odd)
d={}
d['even']=list(filter(lambda x:x%2==0,l))
d['odd']=list(filter(lambda x:x%2!=0,l))
print(d)