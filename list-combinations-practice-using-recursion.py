def combinations(lst,n):
    if n == 0:
        return [[]]
    l =[]
    for i in range(0,len(lst)):
        m = lst[i]
        remlist = lst[i + 1:]
        for p in combinations(remlist,n-1):
            l.append([m, *p])
    return l
print(combinations([1,2,3,4],3))