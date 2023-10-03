# Summary:
# 1. You can use built-in decorators in classes to modify parameters in functions.
# 2. @decorator is the same as function = decorator(function);
# 3. @decorators tend to be used with wrapper inner functions.

# # My Solution
# class MyClass:

#     @staticmethod
#     def some_method():
#         print("this method does nothing with self")


# def our_decorator(some_funct):
#     def wrapper(*args):
#         print("something actually meaningful that we want to do before the function")
#         some_funct(None, *args)
#         print("something actually meaningful that we want to do after the function")
#     return wrapper


# @our_decorator
# def some_function_that_takes_two_parameters(first_param, second_param):
#     print(second_param)


# some_function_that_takes_two_parameters(5)


def my_decorator(some_function):
    def wrapper():
        print("this is the begining")
        some_function()
        print("this is the end. Just be happy")
    return wrapper


@my_decorator
def my_function():
    print("My function")


@my_decorator
def my_second_function():
    print("My second function")


my_function()
my_second_function()
