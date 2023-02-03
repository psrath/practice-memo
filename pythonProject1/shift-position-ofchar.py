s='purn'
#o/p:'rwtp'
res = ''
for ch in s:
    res+=chr(ord(ch)+3)
print(res)

s= 'abc'
shift=[2,3,4]
for ch1 in shift:
    res1=''
    for ch2 in s:
      res1+=chr(ord(ch2)+ch1)
    print(f'SHift of {ch1} result is {res1}')
    s = res1