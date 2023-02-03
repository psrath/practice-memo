#fact = lambda n:n*fact(n-1) if n>1 else n
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         yield fact
# f = fact(5)
# print(f)
# for i in f:
#     print(i)

def fact(n):
    value = 1
    for i in range(1,n+1):
         value *= i
         yield value

f = fact(int(input('Enter the number : ')))
# print(f.__next__())
# print(f.__next__())

for value in f:
    print(value)


