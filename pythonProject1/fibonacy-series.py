fact = lambda n:1 if n<=1 else n*fact(n-1)
print(fact(5))
fibo =lambda n:n if n<=1 else fibo(n-1)+fibo(n-2)
for i in range(5):print(fibo(i),end=' ')
