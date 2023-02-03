def outer_fun(func):
    def inner_fun():
        print('Inside Inner Function')
        return func()
    print('Before Return of outer function')
    return inner_fun
@outer_fun
def wrapper_func():
    print('Inside Wrapper Function')
#var_func=outer_fun(wrapper_func)
#print('Before execution of Outer function')
#var_func()
#print(outer_fun(wrapper_func()))
#func_var=outer_fun(wrapper_func)
#print(func_var())
wrapper_func()
