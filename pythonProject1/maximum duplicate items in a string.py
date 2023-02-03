s= 'purnendusekharrath'
d={}
for ch in s:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
largest=max(d,key=lambda x:d[x])
print(largest+':'+str(d[largest]))