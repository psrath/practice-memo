lst = [2,1,9,0,3,10]

def quicksort(lst):
    if len(lst)<1:
        return lst
    else:
        pivot = lst.pop()
    right_arm=[]
    left_arm=[]
    for ch in lst:
        if ch>pivot:
            right_arm.append(ch)
        else:
            left_arm.append(ch)
    return quicksort(left_arm)+[pivot]+quicksort(right_arm)
res = quicksort(lst)
print(res)
num = int(input('Enter a number'))
if num<res[0]:
    [num]+res
elif num > res[-1]:
    res.append(num)
else:
    for items in range(0,len(res)):
        if res[items]>num:
            break
    res = res[:items]+[num]+res[items::]


print(res)
#print(res)

