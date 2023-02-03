s='purne purnd purpq pura pur'
s1=s.split()
# for i in range(len(s1[0])):
#     char=s1[0][i]
#     for j in range(1,len(s1)):
#         if len(s1[j])==i or char!=s1[j][i]:
#             print(s1[0][:i])


# def prefixstring(s):
#     if not len(s):return ' '
#     for i in range(len(s[0])):
#        char = s[0][i]
#        for j in range(1,len(s)):
#            if len(s[j])==i or char!=s[j][i]:
#             return s[0][:i]
# print(prefixstring(s1))


s1=['purnend','runnend','bandnend','raend']
def subfixstring(s):
    if not len(s):return ''
    for i in range(1,len(s[0])+1):
        char=s[0][-abs(i)]
        for j in range(1,len(s)):
            if len(s[j])==i or char!=s[j][-abs(i)]:
                return s[0][-1:-abs(i):-1][::-1]
print(subfixstring(s1))