# l1=[1,2,3,6,4,5,3]
# l2=[1,2,3,4,5,4,6,7,8,9]
# l3=[]
# for items in l2:
#     if items not in l1:
#         l3.append(items)
# print(l3)
# #comprehension using method
# print([items for items in l2 if items not in l1])
# s= set(l1)
# res = [items for items in l2 if items not in s]
# print(res)

l1=[1,9,5,4,10,12]
l2=[2,3,5,4,12,10]
# common=[items for items in l1 if items in l2]
# print(common)
for items in l1+l2:
    print(items)
lit_diff=[items for items in l1+l2 if items not in l1 or items not in l2]
print(lit_diff)





