while True:
    print('Enter q to Quit')
    x = input('Enter a number')
    if x == 'q':
        break
    try:
        x=int(x)
        if x>6:
            print('u hv enter number > 6')
        else:
            print('u hv enterd no less than 6')
    except Exception as e:
        print(f'You hv entered wrong value {e}')

print('THanks you,Bye Bye')