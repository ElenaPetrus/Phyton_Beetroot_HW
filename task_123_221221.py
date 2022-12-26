from datetime import date

first_name = 'Lena'
second_name = 'Petrus'
full_name = first_name + ' ' + second_name

print(full_name)

day = str(date.today())
want_to_print = 'Good day'+' '+full_name+'!'' '+day + \
    ' '+'is a perfect day to learn some python.'
print(want_to_print)

a = 12
b = 7
print(a+b, a-b, a/b, a*b, a**b, a % b, a//b, sep='\n')
