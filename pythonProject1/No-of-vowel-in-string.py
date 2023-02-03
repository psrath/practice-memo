s='purnendud sekhar RAthUeAio'
vowles='aeiou'
#res = [ch for ch in s if ch in vowles]
#display no of vowels in a string
#print(res)
#How many time which vowel presents
#Way to intialize a dictionary with values
#Below approach take more memory space complexity is more
d={}.fromkeys(vowles,0)
print(d.__sizeof__())
print(d)
for ch in s.casefold():
    if ch in d:
        d[ch]+=1
#Way of Initialize empty dictionary space complexity is less
d1={}
print(d1.__sizeof__())
for ch in s.casefold(): #Ignorecase
    if ch in vowles and ch in d:
        d[ch]=d[ch]+1
    if  ch in vowles and ch not in d:
        d[ch]=1
print(d1.__sizeof__())

for k,v in d.items():
    print(f'{k} presents {v} Times')

