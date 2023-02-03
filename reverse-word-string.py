s = 'my name is purnendu'
#o/p:Purnendu is my name
print(*s.split()[::-1])
s1=s.split()
res =''
for i in range(len(s1)-1,-1,-1):
    res+=s1[i]+' '
print(res)




