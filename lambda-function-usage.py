import functools as ft
#Method1 Using functools reduce
print(ft.reduce(lambda x,y:x*y,range(1,6)))
#Method2 Using lambda function
fact = lambda x: x*fact(x-1) if x >1 else x
print(fact(0))
#Using bruteforce method
fct =1
n=5
while n>1:
    fct*=n
    n-=1
print(fct)
#####################FIB##############################


