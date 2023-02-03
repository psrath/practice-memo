import functools
import itertools as it
l=[1,2,3,4,5,6,5,3]
# l=set(l)
# print(l)
num=10
combi=list(it.combinations(l,3))
print(len(combi))
remove_duplicate=set(map(lambda x:tuple(sorted(x)),combi))
print(sorted(remove_duplicate))
##Using Sum Function
#res = tuple(filter(lambda x:sum(x)==num,remove_duplicate))
##Without Using Sum Function
res =tuple(filter(lambda x:functools.reduce(lambda a,b:a+b,x)==num,remove_duplicate))
print(res)
#res =[items for items in combi if sum(items)==num]
#print(res)
