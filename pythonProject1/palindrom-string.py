s='malayalam'
print('Palindrom') if s==s[::-1] else print('Not Palindrome')
for ch in range(1,len(s)//2+1):
    if s[ch-1]!=s[-abs(ch)]:
        print('Not Palindrom')
        break
else:
    print('Palindrom')