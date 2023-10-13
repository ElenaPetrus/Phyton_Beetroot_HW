# # Task 1
# print('Input no for exit.')
# while True:
#     user_sentance = input('Please write the sentance:')
#     if user_sentance == 'no':
#         break

#     if len(user_sentance) < 2:
#         print('Please write the sentance, that have two letters at least')
#     else:
#         print(user_sentance[:2]+user_sentance[-2:])

# # Task 2
# print('Input no for exit.')
# while True:
#     user_phone_string = input('Please write your phone number: ')
#     if user_phone_string == 'no':
#         break
#     else:

#         if (user_phone_string).isdigit() != 1:
#             print('You phone number should contain ONLY digits.Please try again.')
#         elif len(user_phone_string) != 10:
#             print('your phone number should contain 10 digits. Please try again.')
#         else:
#             print(f'You phone number {user_phone_string} has been saved.')
#             break

# Task 3
stored_name = 'olena'
while True:
    user_name = input('Please write you name:').lower()

    if user_name.isalpha() != 1:
        print('You have normal name only of letters')
    elif user_name != stored_name:
        print('Are you sure that it is your name?')
    else:
        print('You have got access to your bak safe box')
        break
