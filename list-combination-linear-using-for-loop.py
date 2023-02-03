import functools

lst=[8,9,3,2,5,1,6,4,7]
#o/p:[[1,2,3],[4,5,6],[7,8,9]]
d={}
combi = [lst[items:items+3]for items in range(0,len(lst),3)]
print(type(combi))
sum_greatest=functools.reduce(lambda x,y:x if x>y else y,([sum(items) for items in combi]))
print(combi)
print(sum_greatest)