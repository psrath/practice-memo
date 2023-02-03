s= 'aaabbcccdadd'
res=''

for ch in s:
    if ch in res:
        continue
    counter=1
    for ch2 in range(s.index(ch)+1,len(s)):
        if ch==s[ch2]:
            counter+=1
    res+=ch+str(counter)
print(res)

s2='a4b2c3d3'

for ch in range(0,len(s2),2):
    print(s2[ch]*int(s2[ch+1]),end='' '\n')
#Using dictionary
s3='aaabaccddce'
d={}
for ch in s3:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
print(d)

##Reverse a string
s4='purnendu'
print(s4[:-3:-1])
for ch in range(len(s4)-1,-1,-1):
    print(s4[ch],end='')
