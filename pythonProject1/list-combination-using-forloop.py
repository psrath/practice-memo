l=[1,2,3,4,5,6,7,8,9]
#o/p:[(1,2,3),(4,5,6),(7,8,9)]
res = [l[items:items+3:]for items in range(0,len(l),3)]
d={}
for items in res:
    d[sum(items)]=items
print(f'Maximum sum combi element is {max(d)}:::{d[max(d)]}')