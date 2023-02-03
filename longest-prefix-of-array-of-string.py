#s = ['purpurn','purnbcdef','pu','pur']
s = ['purpurnen','purnbcdefen','puen','puren']
def prefixstring(s):
    if not len(s):return ' '
    for i in range(len(s[0])):
       char = s[0][i]
       for j in range(1,len(s)):
           if len(s[j])==i or char!=s[j][i]:
               return s[0][:i]
print(prefixstring(s))



