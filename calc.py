def calc(option,no1,no2):
     match option:
        case '1':
            print(f'Addition of {no1} and {no2} :{no1+no2}')
        case '2':
            print(f'Substraction of {no1} and {no2} :{no1 - no2}')
        case '3':
            print(f'Multiplication of {no1} and {no2} :{no1*no2}')
        case '4':
            print(f'Division of {no1} and {no2} :{no1//no2}')
        case '5':
            exit()

while True:
    x = int(input('Enter 1st Number'))
    y = int(input('Enter 2nd Number'))
    print('1-Addition')
    print('2-Substraction')
    print('3-Multiplication')
    print('4-Division')
    print('5-Exit')
    choice = input('Enter your Choice')
    calc(choice,x,y)
    try:
        z = input('Do you want to continue?[y/n]')
        z=str(z)
        if z == 'n' or z == 'N':
            print('Bye Bye..')
            exit()
    except Exception as e:
        print(e)










