import functools
from collections import Counter

# d3={}
# for k in d1:
#     if k in d2:
#         d1[k]=d1[k]+d2[k]
#     else:
#         pass
# print(d1)
##Using Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#resa = Counter(d1)+Counter(d2)
#print(resa)
res={}
#for i in set(d1).union(d2):
    #res.update({i:d1.get(i,0)+d2.get(i,0)})
res={items: d1.get(items,0)+d2.get(items,0) for items in set(d1)|set(d2)}

print(res)
##add dictionary value with duplicate key items
dict_seq = [
  {'a': 1, 'b': 2, 'c': 3},
  {'a':10, 'b': 20},
  {'b': 100}
]
res = functools.reduce(lambda d1,d2:{k:d1.get(k,0)+d2.get(k,0) for k in set(d1).union(d2)},dict_seq)
#res= functools.reduce(lambda d1,d2:{k:d1.get(k,0)+d2.get(k,0) for k in set(d1)|set(d2)},dict_seq)
#res = functools.reduce(lambda d1, d2 :\
#                       {k:d1.get(k,0)+d2.get(k,0) for k in set(d1)|set(d2)}\
#                       ,dict_seq)
#print(res)
print(res)



