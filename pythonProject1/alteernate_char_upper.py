s='hello world'
res=''
for ch in range(0,len(s)):
    if ch%2==0:
        res+=s[ch].upper()
    else:
        res+=s[ch]
print(res)