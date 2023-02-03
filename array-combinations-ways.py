import itertools as it

from select import error

lt = [1,2,3,4,5]
#Return all posible pair of numbes whose sum is 10
#Using for loop
def returnPairForLoop(lst):
    res = []
    for ch1 in lt:
        for ch2 in range(lst.index(ch1)+1,len(lst)):
                res.append((ch1,lst[ch2]))
    return res
res =set(map(lambda x:x,returnPairForLoop(lt))) #Removes duplicate pairs if list contains duplicate elements
res1 = [items for items in res if sum(items)==10]
print(res1)

##Using itertools
def using_itertool(lt):
    return set(map(lambda x:x,it.combinations(lt,3)))
res = [items for items in using_itertool(lt) if sum(items)==10]
try:
    if not len(res):
        raise TypeError
except TypeError:
    print('No pair found of sum 10')
else:
    print(res)

