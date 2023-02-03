d={7:6,2:1,1:3,3:7,4:8,5:5,6:4}
#d.pop(7)
#d[7]=6
#d.__setitem__(8,7)
#d=sorted(d.items(), key=lambda x : x[1],reverse=True)
#res_max=max(d,key=lambda x:x[1])
#print(res_max)
#print(d)
sorted_key=sorted(d,key=lambda x : x[1])
print(sorted_key)