a,b=0,1
print(a)
num =10
count =0
while count<num-1:
    print(b)
    a,b=b,a+b
    count+=1
def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(10):
    print(fibo(i))