import itertools as it
lt = [1,2,3,4,5,6,7,8,9]
combi = []
for i in range(len(lt)-1):
    for j in range(i+1,len(lt)):
       combi.append(int(str(lt[i])+str(lt[j])))
print(combi)
#res = [int(f"{x}{y}") for x,y in combi]
#print(res)
#res =list(filter(lambda x:sum(x)==10,list(it.combinations(lt,3))))
#res1 = [items for items in list(it.combinations(lt,2)) if sum(items)==10]
#print(res)