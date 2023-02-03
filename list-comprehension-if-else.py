import functools as ft

# res = {i:i*i if not i%2 else i*i*i for i in range(1,10)}
# print(res)
# sum = [i for i in range(1,10)]
# #print(functools.reduce(lambda x,y:x+y,range(1,10)))
#
# lst =[3,2,5,1,5,0,3,2,1]
# combi = [lst[i:i+3:] for i in range(0,len(lst),3)]
# summ = [ft.reduce(lambda x,y:x+y,items) for items in combi]
# maximum = max(summ)
# print(maximum)
def quick(lt):
    if len(lt)<1:
        return lt
    else:
        pivot = lt.pop()
    letf_Arm = []
    right_arm = []
    for items in lt:
        if items > pivot:
            right_arm.append(items)
        else:
            letf_Arm.append(items)
    return quick(letf_Arm)+[pivot]+quick(right_arm)
res = quick([3,0,5,-1,11,9,4,8])
print(f'After sorting: {res}')
num=6
res1= []
for i in range(0,len(res)):
    if res[i]>num:
       print(res[:i:]+[num]+res[i::])
    break
print(res)
# num = int(input('Enter a number'))
# if num <res[0]:
#     res=[num]+res
# elif num > res[-1]:
#     res.append(num)
# else:
#     for items in range(0,len(res)):
#         if res[items]>num:
#             res[:items:]+[items]+res[items::]
#print(f'After Insertion: {res}')

# st = 'aabcdadeffgh'
# d={}
# for ch in st:
#     if ch in d:
#         d[ch]=d[ch]+1
#     else:
#         d[ch]=1
# maxi = max(d,key=lambda ch : d[ch])
# print(maxi+':'+str(d[maxi]))
# print(d)
#
# res =''
# for ch in st:
#     if ch not in res:
#         res+=ch+str(st.count(ch))
# print(res)
# res2 =''
# for ch1 in st:
#     if ch1 in res2:
#         continue
#     counter=0
#     for ch2 in range(st.index(ch1),len(st)):
#         if ch1==st[ch2]:
#             counter+=1
#     res2+=ch1+str(counter)
# print(res2)










