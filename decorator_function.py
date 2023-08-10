def eshani(original_function):
    def wrapper_function(*args, **kwargs):
        # Perform additional actions before the original function
        print("instruction label")
        result = original_function(*args, **kwargs)
        # Perform additional actions after the original function
        print("gift from nick")
        return result
    return wrapper_function

@eshani
def greet(name,lname):

    print(f"Hello, {name}!")

greet("Alice","smith")

@eshani
def hi(name,number):
    print(f"Hello, {name} {number}!")

hi("alice",6)
