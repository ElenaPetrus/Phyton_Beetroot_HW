#  Task 1
def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(
            f"{key}={value!r}" for key, value in kwargs.items())
        print(
            f"{func.__name__} called with {args_str}{', ' if args and kwargs else ''}{kwargs_str}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# print(add(4, 5))
# print(square_all(4, 5))

# Task2
def stop_words(words):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, '*')
            return result
        return inner_wrapper
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# print(create_slogan('Steve'))

# Task3


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check the number of arguments
            if len(args) != 1 or kwargs:
                print("Invalid number of arguments.")
                return False

            argument = args[0]

            # Check the type
            if not isinstance(argument, type_):
                print(
                    f"Invalid type. Expected {type_}, got {type(argument).__name__}.")
                return False

            # Check the maximum length
            if len(argument) > max_length:
                print(f"Length exceeds the maximum allowed ({max_length}).")
                return False

            # Check if it contains the required symbols
            for symbol in contains:
                if symbol not in argument:
                    print(f"Missing required symbol: {symbol}.")
                    return False

            # If all checks pass, call the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# print(create_slogan('@Steve05'))
