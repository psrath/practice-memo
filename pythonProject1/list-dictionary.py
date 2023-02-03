l1=['a', 'b', 'c', 'd', 'e', 'f']
l2=[1, 2, 3, 4, 5]
res=dict(zip(l1,l2))
d={}
for i in range(0,len(l2)):
    d[l1[i]]=l2[i]
print(d)
print(res)