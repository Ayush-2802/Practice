def toll_func(func):
    def wrapper(*args,**kwargs):
        args_v = ', '.join(str(args) for arg in args)
        kwargs_v = ', '.join(f"{key},{value}" for key,value in kwargs.items())
        print(f"Function:{func.__name__} \nArguments:{args_v},{kwargs_v}")
        return func(*args,**kwargs)
    return wrapper

@toll_func
def greet(name,greetings = "hello"):
    print(f"{greetings},{name}")

greet("ayush",greetings="hanji")