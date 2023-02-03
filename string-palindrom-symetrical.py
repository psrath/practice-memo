s='malayalamm'
print(len(s))
print(len(s)//2)
# if s == s[::-1]:
#     print('palindrom')
n=len(s)-1
for ch in range(0,len(s)//2):
    if s[ch]!=s[n]:
        print('Not Palidrom')
        break
    n-=1
else:
    print('palindrom')
##Check string is symetric or not
s2 = 'madma'
if not len(s2)%2:
    if s2[0:len(s2)//2:]==(s2[len(s2)//2::]):
        print('Symetrical')
    else:
        print('Not symetrical')
else:
    if s2[0:len(s2)//2:]==(s2[len(s2)//2+1::]):
        print('Symetrical')
    else:
        print('Not symetrical')


