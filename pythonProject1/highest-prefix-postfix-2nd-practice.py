#s= 'purnendu purn purudu purn pur'
s= 'purnendup srdup abdup dup strefdup up'
s1=s.split()
print(s1)
# def highPrefix(s):
#     for i in range(len(s[0])):
#         char=s[0][i]
#         for j in range(1,len(s)):
#             if len(s[j])==i or char!=s[j][i]:
#                 return s[0][:i]
# print(highPrefix(s1))
def postFix(s):
    for i in range(1,len(s[0])+1):
        char=s[0][-abs(i)]
        for j in range(1,len(s)):
            if len(s[j])==i or char != s[j][-abs(i)]:
                return s[0][:-abs(i+1):-1][::-1]

print(postFix(s1))
