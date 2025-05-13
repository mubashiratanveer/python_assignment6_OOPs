def log_function(func):
    def wraper():
        print("Function is being called.")
        return func()
    return wraper


@log_function
def say_hello():
    print("Hello!")

say_hello()