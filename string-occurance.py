s='aaabbcccddeeeeaa'
d={}
for items in s:
    if items in d:
        d[items]=d[items]+1
    else:
        d[items]=1
print(d)
for values in d.values():
    print(values)
# maximum_alpha=max(d.items(),key=lambda x:x[1])
# print(maximum_alpha)