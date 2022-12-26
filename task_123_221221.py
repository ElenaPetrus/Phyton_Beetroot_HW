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
want_to_print = 'Good day {}! {} is a perfect day to learn some python.'
print(want_to_print.format(full_name, day))


a = 12
b = 7
print(a+b, a-b, a/b, a*b, a**b, a % b, a//b, sep='\n')
