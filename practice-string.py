s = 'heliliLo world'
res = ''
for ch in range(len(s)):
    if ch%2==0:
        res+=s[ch].upper()
    else:
        res+=s[ch]
print(res)
#String compression
#input='aabbccdddeef'
#output=abcdef and a2b2c2d3e2f1
compress_res=''
input='aabbccdddeefa'
for ch in input:
    if ch not in compress_res:
        compress_res+=ch
print(compress_res) #o/p:abcdef
compression=''
for ch1 in input:
    if ch1 in compression:
        continue
    counter = 0
    for ch2 in range(input.index(ch1),len(input)):
        if ch1 == input[ch2]:
            counter+=1
    compression+=ch1+str(counter)
print(compression) ## O/P: a3b2c2d3e2f1
##ANother way by count function
new_compression=''
for ch in input:
    if ch not in new_compression:
        new_compression+=ch+str(input.count(ch))
print(new_compression) # O/P:a3b2c2d3e2f1
##Using Dictionary
d ={}
for ch in input:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
for ch in d:print(ch+':'+str(d[ch]),end=' ')

inpt= 'a3b2c1'
output=''
print('\n')
for ch in range(0,len(inpt),2):
     output+=inpt[ch]*int(inpt[ch+1])
print(output) #aaabbc

#Reverse a string
s1 = 'Purnendu'
print(s1[::-1])
#Reverse each word in a Sentence
s2 = 'Purnendu Sekhar Rath'
res_1=''
for ch in s2.split():
    res_1+=ch[::-1]+' '
print(res_1)
##
#o/p:Rath Sekhar Purnendu
#Method1
print(*s2.split()[::-1])
#Method2
res_2=''
s3 =s2.split()
for ch in range(len(s3)-1,-1,-1):
    res_2+=s3[ch]+' '
print(res_2)
for i in range(len(s)-1,0):print(s2[-abs(i)],end=' ')
#Count the maximum repetative character in a string
s_count='AbcAdd aaddBc cEDE'.lower().replace(' ','')
print(s_count)
d={}
for ch in s_count:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1

char_max = max(d,key=lambda x:d[x])

print(d)
print(f'Highest occuranace char is : {char_max} :Presents:{d[char_max]} Times')
highest_2= sorted(set(d.values()))[-3]
print(highest_2)
max=0
for v in d.values():
    if v>max:
        max=v
print(max)
##Program to find Min subfix from a array of string
s_str=['purabcd','purnpq','purhjg','purn']
def longSubfix(s):
    if len(s)==0:return s
    for i in range(0,len(s_str[0])):
        search=s_str[0][i]
        for j in range(1,len(s_str)):
            if len(s_str[j])==i or s[0][i]!=s[j][i]:
                return s_str[0][:i]
print(longSubfix(s_str))









