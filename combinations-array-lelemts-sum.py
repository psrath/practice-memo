'''Program to take a list of integer, make a combinations of number e.g
2 or 3 .. n=integer and make a sum of those combination and print a new list
print only numbers whose sum is even or odd
'''
import functools as ft
import more_itertools as mt
import numpy as np
arr = [1,2,3,4,5,6,7,8,9]
# def makeCombinations(arr,combinations):
#     if not len(arr)%combinations == 0:
#         raise TypeError('Combinations is not correct\nCombinations should be divisible by length of array\nPls enter corect combinations')
#     res = [arr[items:items+combinations:]for items in range(0,len(arr),combinations)]
#     return res
# def makeCombinationsUsingMoreIterTools(arr,combinations):
#     return list(mt.chunked(arr,combinations))
# def makeCombinationsUsingNumPy(arr,combinations):
#     return np.array_split(arr,combinations)
# print(makeCombinationsUsingNumPy(arr,3))
# res = [sum(items) for items in makeCombinationsUsingNumPy(arr,3)]
# print(res)

#print(makeCombinationsUsingMoreIterTools(arr,2))
#print(makeCombinations(arr,3))
#res = [sum(items) for items in makeCombinations(arr,2)]
#print(res)
#make a combination of array according to the number here combinations of 3 is done
# res1 = [arr[cnt:cnt+3:] for cnt in range(0,len(arr),3)]
# ##Method1 using no built in methods
# for items in res1:
#     sum1 = 0
#     for digit in items:
#         sum1 += digit
#     res.append(sum1)
# print(res)
#
# ##Using sum method in list comrehension
# res3 = [sum(items) for items in res1]
# print(res3)
#
def listcombinations(arr,combinations):
    res = [arr[items:items+combinations:] for items in range(0,len(arr),combinations)]
    return res
#print(listcombinations(arr,3))
res_sum =[sum(items) for items in listcombinations(arr,3)]
#max = ft.reduce(lambda x,y:x if x>y else y,res_sum)
even = list(filter(lambda x :x % 2 ==0 ,res_sum))
print(even)
#print(max)
maximum = res_sum[0]
for i in res_sum:
    if i >maximum:
        maximum = i
#print(maximum)
#print(max(res_sum))

l1 = [1,2,3,4,5,6,7,8,9]
res = [l1[x:x+3:] for x in range(0,len(l1),3)]
print(res)
max = max(res,key=lambda x : sum(x))
print(sum(max))

sr = 'purnendu'
res = ''
for ch in sr:
   if ch not in res:
       res+=ch
