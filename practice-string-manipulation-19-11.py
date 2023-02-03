str123 = 'aaabbcdefa'
res = ''
####Alternate character to Upper letter
for ch in range(0,len(str123)):
    if ch % 2 == 0:
        res += str123[ch].upper()
    else:
        res += str123[ch]
print(res)
###Print howmany times a character is present in a string e.g a4b2c3d1e1f1
res1 =''
for ch1 in str123:
    if ch1 in res1:
        continue
    counter =0
    for ch2 in range(str123.index(ch1),len(str123)):
        if ch1 == str123[ch2]:
            counter +=1
    res1 +=str(counter)
print(res1)

###Same above qstn using dictionary
ss='ppurrrneedddupu'
d = {}
for ch in ss:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
print(d)
res = ''
for k,v in d.items():
    res+=k+str(v)
print(res)
##Using Count function
st = 'aaabbcccddeeea'
ress =''
for ch in st:
    if ch not in ress:
        ress += ch + str(st.count(ch))
print(ress)

##2ndtime practice:
s1 = 'aaabaaccdeeefa'
# res3 = ''
# for ch1 in s1:
#     if ch1 in res:
#         continue
#     counter = 0
#     for ch2 in range(s1.index(ch1),len(s1)):
#         if ch1 == s1[ch2]:
#             counter+=1
#     if ch1 not in s1:
#         res3+=ch1+str(counter)
# print(res3)
###Using Dictionary
d1 = {}
for c in s1:
    if c in d1:
        d1[c]=d1[c]+1
    else:
        d1[c] = 1
print(d1)

st='Purnendu Sekhar Rath'
r = ''
for ch in st.split(' '):
    for c in range(0,len(ch)):
        if c%2==0:
            r+=ch[c].upper()
        else:
            r+=ch[c]
    r+=' '
print(r)






