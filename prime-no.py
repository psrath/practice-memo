###No is a Prime no or not
###Method1
num=int(input('Enter a number > 1'))
#counter =0;
##For loop in a single line
# for i in range(1,num+1):
#     if num % i == 0:
#         counter+=1
# if counter == 2:
#     print('Prime Number')
# else:
#     print('Not Prime Number')
#Write in a single line of if condition
#print('Prime Number') if counter == 2 else print('Not a Prime Number')

##Method2
for i in range(2,num//2+1):
    if num %i ==0:
        print('Not Prime')
        break
else:
    print('Prime Number')
