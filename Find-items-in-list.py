lst = [10,12,14,15,16]
#copy_list=lst
#print(copy_list)
item_to_find = 20
if item_to_find  in lst:
     print('Item Present')
else:
    print('Items Not present')

#copy list using list comprehension
list_copy =[i for i in lst]
print(list_copy)