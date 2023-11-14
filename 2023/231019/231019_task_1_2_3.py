# # Task 1
# def favorite_movie():
#     name = str(input('What is you faforite movie? '))
#     print(f'My favorite movie is named \'{name}\'')

# favorite_movie()

# # # task 2
# def make_country(name, capital):
#     country_dict = {'country_name': name, 'capital': capital}
#     return country_dict

# print(make_country('Ukraine', 'Kyiv'))

# task 3
def make_operation(operator, *args):
    result = args[0]
    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num
    elif operator == '*':
        for num in args[1:]:
            result *= num

    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
