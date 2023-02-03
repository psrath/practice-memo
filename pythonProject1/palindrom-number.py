num=3553
def palindrome(num):
    rev = 0
    while num>0:
        rem=num%10
        rev = (rev*10)+rem
        num=num//10
    return rev
if num == palindrome(num):
    print('palindrome')
else:
    print('Not')

