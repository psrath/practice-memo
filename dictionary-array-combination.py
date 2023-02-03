import itertools as it
sample={'1':['a','b'], '2':['c','d']}
res1=[values for values in sample.values()]
print(len(res1))
res=[]
for items in range(0,2):
    res.append(res1[0][items]+res1[1][0])
    res.append(res1[0][items]+res1[1][1])
print(res)






