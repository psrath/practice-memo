import functools
import itertools as it
lst = [1,2,3,4,5,6]
res = [items for items in list(it.combinations(lst,3)) if sum(items)==10]
print(res)