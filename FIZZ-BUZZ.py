
res=''
def printRes(n):
    d = {3: 'FIZZ', 5: 'BUZZ'}
    res=''
    for items in d:
        if n%items==0:
            res+=d[items]
    return res
for i in range(1,100):
    if printRes(i):
        print(f'{i}::{printRes(i)}')



