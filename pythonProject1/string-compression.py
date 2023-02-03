s = 'aaaaabbccdde'
# s1=''
# for ch in s:
#     if ch not in s1:
#         s1+=ch
# print(s1)
#o/p:a4b3c2d1
# s2=''
# for ch in s:
#     if ch in s2:
#         continue
#     counter=0
#     for ch2 in range(s.index(ch),len(s)):
#         if ch==s[ch2]:
#             counter+=1
#     s2+=ch+str(counter)
# print(s2)
#Using dictionary
d={}
for c in s:
    if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1
print(d)
s2='a3b2c3d1'
s3=''
for ch in range(0,len(s2)-1,2):
    s3+=s2[ch]*int(s2[ch+1])
print(s3)