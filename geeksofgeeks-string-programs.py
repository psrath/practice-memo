import os.path as op
#Reverse words in a given string
#str = 'Reverse words in a given string'
#res =''
# s = str.split()[::-1]
# print(*s)
# for i in range(1,len(s)+1):
#     res+=s[-abs(i)]+' '
# print(res)
# res += str[]
res=[]
# s=str.split()
# print(s)
# for ch in range(len(str.split())-1,-1,-1):
#     res+=s[ch]+' '
# print(res)
# for w in s:
#     res.insert(0,w)
# print(*res)

#s1 =list(s)
#print(s[0][0])
# print(s1)
s = ["geeksforgeeks", "geeks", "gee", "geeze","ge"]
def resstr(s):
    for i in range(len(s[0])):
        ch = s[0][i]
        for j in range(1,len(s)):
            if i == len(s[j]) or s[j][i]!=ch:
                return s[0][:i]
print(resstr(s))
print(op.commonprefix(s))



