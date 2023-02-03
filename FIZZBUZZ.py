def fizzbuzz(n):
    d={3:'FIZZ',5:'BUZZ'}
    res=''
    for k,v in d:
        if n%k == 0:
            res += v
    return res
# for i in range(1,100):
#     if fizzbuzz(i):
#         print(f'{i}::{fizzbuzz(i)}')
###FIZZBUZZ Using Generator
def fizzbuzzIF(n):
    res=''
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            yield 'FIZZBUZZ'
        elif i%3 == 0:
             yield 'BUZZ'
        elif i%5 == 0:
            yield 'FIZZ'
        else:
            pass
# rng = int(input('Enter a Number upto shown String'))
# for items in fizzbuzzIF(rng):
#     print(items)

##Normal IF Else
for i in range(1,101):
    if i%3 == 0 and i%5==0:
        print(f'{i}::FIZZBUZZ')
    elif i%3 == 0:
        print(f'{i}::FIZZ')
    elif i%5 == 0:
        print(f'{i}::BUZZ')
    else:
        pass



