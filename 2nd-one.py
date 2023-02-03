lst=[1,2,3,4,5,2,3]
#count # of element presents
#Using count Function
res1=set([items for items in lst if lst.count(items)>1])
print(res1)
##Using Dictionary
d={}
for items in lst:
    if items in d:
        d[items] += 1
    else:
        d[items] = 1
res = []
for k,v in d.items():
    if v>1:
        print(f'{k} presents {v} Times')
        res.append(k)
print(res)
##Remove Duplicate element
res = []
for items in lst:
    if lst.count(items)>1 and items not in res:
        res.append(items)
print(res)



