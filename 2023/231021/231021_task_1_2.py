# #  Task 1
# def oops():
#     raise KeyError('This is an KeyError')


# def catch_error():
#     try:
#         oops()
#     except IndexError as e:
#         print(f'Caught an IndexError: {e}')


# catch_error()
# # have the result KeyError: 'This is an KeyError'))))


#  task 2
def calculate_squared_division():
    try:
        a = float(input('Enter the value of a: '))
        b = float(input('Enter the value of b: '))

        result = (a ** 2) / b
        return result

    except ZeroDivisionError as zde:
        print(f'Error:{zde}. Can not divide by 0. Skipping...')
    except ValueError as ve:
        print(f'Error:{ve}.Not an integer. Skipping...')


calculated_result = calculate_squared_division()
if calculated_result is not None:
    print(f"The result is: {calculated_result:.2f}")
