n=371
# def amstrong(n):
#     res =0
#     while n>0:
#         rem=n%10
#         res+=rem*rem*rem
#         n=n//10
#     return res
# if n==amstrong(n):
#     print('Amstrong Number')
# else:
#     print('Not a Amstrong Number')

#using lambda and list
l1 =list(map(int,str(n)))
print(l1)
l2=sum(map(lambda x:x**3,l1))
print(l2)