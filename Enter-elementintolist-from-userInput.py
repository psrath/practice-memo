import functools as ft
arr = list(map(int,input('Enter , speprated num').split(',')))

#arr2 = [ int(num) for num in input(' Enter , seperated number ').split(',') ]
##Using reduce function and lambda
print(arr)
# sum = ft.reduce(lambda x,y:x+y,arr)
# print(f'Sum is: {sum}')

###Using for loop
# sum = 0
# for i in arr: sum += i
# print(f'Sum is:: {sum}')

##Using Builtin sum function
print(sum(arr))