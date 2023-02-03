s='purnendu sekhar rath'
print(*s.split()[::-1])

#Using For loop
s1=s.split()
res = ''
for ch in range(len(s1)-1,-1,-1):
    res+=s1[ch]+' '
print(res)

#Reverse word in a string
res1=''
for ch in s.split():
    res1+=ch[::-1]+' '
print(res1)