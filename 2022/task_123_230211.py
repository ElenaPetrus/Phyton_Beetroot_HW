# Modify the recursive function in order to make it print "start" exactly 5 times

# you can put something here as well

# def recursive_function():  # you can modify this line as well
#     # you can put something here
#     print("start")  # but don't modify this one (no putting it inside a loop or whatever)
#     recursive_function()  # you can modify this line instead
#     # and put something here


# recursive_function()
def print_function(n, text):
    if n == 0:
        print('I cannot print more')
    else:
        print(f'{text}')
        return print_function(n-1, text)


print_function(5, 'cat')
