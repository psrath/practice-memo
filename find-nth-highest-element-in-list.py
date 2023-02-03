lst = [10,3,1,5,19,4]
def sortList(lst):
      for i in range(0,len(lst)-1):
        for j in range(0,len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
      return lst
def findNthlargeElement(lst,sortedList,position):
    #sortList(lst)
    res = sortedList(lst)
    return res[-abs(position)]
print(findNthlargeElement(lst,3))

