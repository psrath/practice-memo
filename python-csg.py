for items in range(1,100):
    if items % 3 == 0 and items % 5 == 0:
        print(f'{items}::FIZZBUZZ')
    elif items % 3 == 0:
        print(f'{items}::FIZZ')
    elif items % 5 == 0:
        print(f'{items}::BUZZ')
    else:
        pass

###2nd Way
def printFunc(n):
    d={3:'Fizz',5:'Buzz'}
    res = ''
    for k in d:
        if n%k == 0:
           res+=d[k]
    return res
#print(printFunc(30))

###Using For Loop
d={3:'FIZZ',5:'BUZZ'}
# for no in range(1,100):
#     res=''
#     for k in d:
#         if no%k == 0:
#          res+=d[k]
#     if res:
#         print(f'{no}:::{res}')


