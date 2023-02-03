import functools as ft
###Factorial of a Number
##Method1 using while loop
num = int(input('Enter a Number'))
#fact = 1
# while num > 0:
#     fact *= num
#     num -= 1
# print(fact)
##Using For Loop
# for i in range(num,0,-1):
#     fact *= i
# print(fact)
###Using reduce function
fact = ft.reduce(lambda x,y:x*y ,range(1,num+1))
print(fact)

##Using recursion
# def fact(num):
#     if num <=1:
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(num))
