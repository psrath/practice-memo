import functools as ft
arr = list(map(int,input('Enter array Numbers ').split(',')))
print(f'Array is :: {arr}')
# big = ft.reduce(lambda x,y:x if x>y else y,arr)
# print(f'Big Number is :: {big}')
# small = ft.reduce(lambda x,y:x if x<y else y,arr)
# print(f'Small Number is :: {small}')

##Another method
max =arr[0]
for i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)

