def add(*args, **args1):
    sum = 0
    for i in args:
        sum+=i
    print(f'Sum of Numbers is :{sum}')
    for items in args1:
        print(items +':' +args1.get(items))

#print(add(1,2,3,4))
add(1,2, Name= 'Purnendu',Age='29',sex='m')