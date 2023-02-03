lst = [-2,5,-1,3,2,9,7,0,8]
def quickSort(lt):
    if len(lt)<1:
        return lt
    else:
        pivot = lt.pop()
    left_arm=[]
    right_arm=[]
    for items in lt:
        if items>pivot:
            right_arm.append(items)
        else:
            left_arm.append(items)
    return quickSort(left_arm)+[pivot]+quickSort(right_arm)


print(quickSort(lst))
