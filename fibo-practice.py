# a,b =0,1
# print(a,end=' ')
# n=10
# while(n>0):
#     print(b,end=' ')
#     a,b =b,a+b
#     n-=1

fib = lambda n:n if n<=1 else fib(n-1)+fib(n-2)
for i in range(10):print(fib(i),end=' ')

fact=lambda x:x if x<=1 else x*fact(x-1)
print(f'\n{fact(5)}')
