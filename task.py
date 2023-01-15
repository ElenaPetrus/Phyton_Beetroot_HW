
# user_num = int(input("Enter a number between 0 and 100: "))


# while user_num >= 0 and user_num <= 100:
#     if user_num % 5 == 0 and user_num % 3 == 0:
#         print("your number is mul_three and mul_five as well")
#     elif user_num % 5 == 0:
#         print("your number is mul_five")
#     elif user_num % 3 == 0:
#         print("your number is mul_three")
#     else:
#         next_question = int(
#             input("If you want to continue print 'yes', If you want to spot print 'No'"))
#         if next_question == "yes":

#     while True:
#     question = "please provide a number between 1 to 100 or print 'stop' to stop"
#     user_input = input(question)
#     if user_input == "stop":
#         break
#         if user_input % 3 == 0:
#             print(" It is Mul_three")
#         elif user_input % 5 == 0:
#             print("it is mul_five")
#         elif user_input % 3 == 0 and user_input % 5 == 0:
#             print("This is both Mul_three and Mul_five")
#         else:
#             print("it is neither mul_three or Mul_five")

print("Input [no] for exit.")

while True:
    inp = input("Please write phone number: ")
    if inp == 'no':
        break
    # catch any resulting ValueError during the conversion to float

    else:

        if (inp).isdigit() != 1:
            print('You phone number should contain ONLY digits.Please try again.')
        elif len(inp) != 10:
            print('your phone number should contain 10 digits. Please try again.')
        else:
            print('everything is very strange.')
