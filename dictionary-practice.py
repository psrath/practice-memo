##Sorted a dictionary by it's value
#Ascending
# d={7:6,2:1,1:3,3:7,4:8,5:5,6:4}
# asc_dict=sorted(d.items(),key=lambda x:x[1])
# print(f'Ascending dict by value is {asc_dict}')
#Desending
# dsc_dict=sorted(d.items(),key=lambda x:x[1],reverse=True)
# print(f'Descending dic by values is {dsc_dict}')
#======================================================
##Adding a key into Dictionary
#d={0: 10, 1: 20}
#Method1
#d[2]=30
#method2
# d.update({5:50})
# print(d)
#Method3
# d.__setitem__(3,40)
# print(d)

##Concatenate Dictionary
import functools

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(dic1|dic2|dic3)
print({**dic1,**dic2,**dic3})
dict3={**dic1,**dic2,**dic3}
print(dict3)
dict4={}
for d in (dic1,dic2,dic3):
    dict4.update(d)
print(dict4)
#dic1.update(dic2)
#dic1.update(dic3)
#print(dic1)
###Check given key exists in dictionary or not
d_key={'name':'purnendu','age':25,'sex':'male','height':4.5}
if 'name' in d_key:
    print('PASS')
else:
    print('FAIL')
##Iterate over dictionary using for loop
for k,v in d_key.items():
    print(f'{k} is {v}')

##Write a program to square of numbers with values upto a range
## like: {1:1,2:4,3:9}
def dict_sqr(no,type):
    if type=='forloop':
        d={}
        for items in range(1,no+1):
            d[items]=items**2
        return d
    if type=='comprehension':
        return {items:items**2 for items in range(1,no+1)}
print(dict_sqr(5,'comprehension'))
######Sum all the items in teh dictionary
d1={'rahul':10,'rama':20,'shyam':30,'radha':30}
res1=sum(d1.values())
res2=functools.reduce(lambda x,y:x+y,d1.values())
print(res2)
sum=0
for items in d1.values():
    sum+=items
print(sum)
######Multiplication all the items in teh dictionary
res_mul=functools.reduce(lambda x,y:x*y,d1.values())
print(res_mul)
mul=1
for items in d1.values():
    mul *= items
print(mul)
###Delete a perticular items from a list
d2={'kishori':10,'rama':20,'shyam':30,'radha':30}
#d2.popitem('radha')
if 'shyam' in d2:
    del d2['shyam']
#d2.__delitem__('radha')
print(d2)
##create dictionary from two array
lst1 = ['a','b','c','d','e']
lst2 = [2,4,1,9,6]
d={}
for i in range(0,len(lst1)):
    d[lst1[i]]=lst2[i]
print(d)
print(dict(zip(lst1,lst2)))
##Sort a given dictionary by key
dd={1:10,4:11,5:12,2:3,6:5}
##Sorted by values
res4=dict(sorted(dd.items(),key=lambda x:x[1],reverse=True))
print(f'Sorted By Values:: {res4}')
##Sorted By keys
print(f'Sorted by key:: {dict(sorted(dd.items(),reverse=True))}')
##Maximum keys from a dictionary
res_max=max(dd)
res_min=min(dd)
res_max_values=max(dd.items(),key=lambda x:x[1])
res_min_values=min(dd.items(),key=lambda x:x[1])
print(f'Minimum value in Dict:: {res_min_values}')
print(f'Maximum value in Dict:: {res_max_values}')
print(f'Maximum key in Dict:: {res_max}')
print(f'Minimum key in Dict:: {res_min}')


