###Fibonacy series program
def fibo(num):
    a,b = 0,1
    temp = 0
    print(a)
    while temp < num:
        print(b)
        temp = a+b
        a=b
        b=temp
#fibo(10)
##Not using temporary variable
# def fibo2(num):
#     a,b = 0,1
#     print(a)
#     while b < num:
#         print(b)
#         a,b = b,a+b
# fibo2(10)
#Print fibo upto nth position
def fibo3(position):
    a,b = 0,1
    print(a,end=' ')
    for _ in range(1,position):
        print(b,end=' ')
        a,b = b,a+b
fibo3(10)
def fibo_recur(num):
    if num <=1:
        return num
    else:
        return fibo_recur(num-1)+fibo_recur(num-2)
print(f'\n')
for i in range(10):
    print(fibo_recur(i),end=' ')
###Using lambda function
fib = lambda n:n if n<=1 else fib(n-1)+fib(n-2)
print(f'\n')
for i in range(10):print(fib(i),end=' ')




