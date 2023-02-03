def calculator(func):
    def wrapper_calc(*args):
        print('Calculator Program statrs')
        rv = func(*args)
        print('Sum of number is:')
        return rv
    return wrapper_calc
@calculator
def outer_function(x,y,z):
    print(x,y,z)
    return x+y+y

print(outer_function(5,3,7))
print('calculator program end')
