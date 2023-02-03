def sortQuick(l):
    if len(l)<1:
        return l
    else:
        pivot = l.pop()
    l_arm=[]
    r_arm=[]
    for items in l:
        if items>pivot:
            r_arm.append(items)
        else:
            l_arm.append(items)
    return sortQuick(l_arm)+[pivot]+sortQuick(r_arm)
l=[1,4,2,0,-1,7]
print(f'2nd Highest salary is {sortQuick(l)[-2]}')