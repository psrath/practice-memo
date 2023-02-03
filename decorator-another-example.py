def dec(str):
    def wrapper():
        print("Inside Wrapper")
        print(str)
        print('End of wrapper')
    print('Inside decorator function')
    return wrapper

x =dec('Purnendu')
print('After calling decorator function')
x()


