# Task 1 & Task 2

from datetime import date

first_name = 'Lena'
second_name = 'Petrus'
full_name = first_name + ' ' + second_name

print(full_name)

day = str(date.today())
# option 1
# want_to_print = 'Good day'+' '+full_name+'!'' '+day + \
#    ' '+'is a perfect day to learn some python.'
# print(want_to_print)

# option 2
# want_to_print = f'Good day {full_name}! {day} is a perfect day to learn some python.'
# print(want_to_print)

# option 3
# want_to_print = 'Good day {}! {} is a perfect day to learn some python.'
# print(want_to_print.format(full_name, day))

# option 4
want_to_print = 'Good day {1}! {0} is a perfect day to learn some python.'
print(want_to_print.format(day, full_name))

# Task 3
a = int(input('Enter fist number: '))
b = int(input('Enter second number: '))
print(a+b, a-b, a/b, a*b, a**b, a % b, a//b, sep='\n')
