import itertools as it
l=[1,2,3,4,5,6]
fact = lambda x:1 if x<=1 else x*fact(x-1)
print(fact(5))
comb_iter=list(it.combinations(l,3))
print(len(comb_iter))
def combi(arr,comb):
    if comb==0:
        return [[]]
    l=[]
    for i in range(0,len(arr)):
        first=arr[i]
        rem=arr[i+1:]
        for p in combi(rem,comb-1):
            l.append([first,*p])
    return l
print(len(combi(l,3)))
res=[(l[i],l[j],l[k])for i in range(0,len(l)) for j in range(i+1,len(l)) for k in range(j+1,len(l)) if l[i]!=l[j]!=l[k]]
print(len(res))
