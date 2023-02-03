'''program to find the combinations of numbers whose sum is a perticular number
given a list of numbers  , i want all combinations of numbers from the list a new list
whose addition value is 10'''
import itertools as it
arr =[1,2,3,4,2,3]
res = list(it.combinations(arr,3))
print(res)
print(len(res))
res_remove_duplicate=set(map(lambda x: tuple(sorted(x)),res))
print(len(res_remove_duplicate))
print(res_remove_duplicate)
sum_array = [items for items in res_remove_duplicate if sum(items)%2==0]
print(sum_array)
# res = []
# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#         res.append((arr[i],arr[j]))
# print(res)
# print(len(res))
# s1 = set()
# sum_res = []
# for items in res:
#     if sum(items) == 5 and items[0] not in s1:
#         sum_res.append(items)
#         s1.add(items[0])
#         s1.add(items[1])
# print(s1)
#sum_res = [items for items in res if sum(items) == 5 ]
#print(sum_res)