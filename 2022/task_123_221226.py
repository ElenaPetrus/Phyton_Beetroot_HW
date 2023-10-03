# # task1
# import random

# correct_number = random.randint(0, 10)
# question = 'Try to gues the number between 0 and 10?'
# print('Let\'s play the guessing game!')

# while True:
#     guess = int(input(question))

#     if guess < correct_number:
#         print('Little higher')
#     elif guess > correct_number:
#         print('Little lower')
#     else:  # guess == answer
#         print('You are the MINDREADER!!!')
#         break
# # task2
# name = input("Enter your name: ")
# while True:
#     try:
#         current_age = int(input("Enter your age: "))
#         break
#     except ValueError:
#         print("No valid age! Please try again ...")
# future_age = current_age+1
# print(f"Hello {name}, on your next birthday you’ll be {future_age} years")


# # # task3
# import random
# question = 'Please type any word: '
# user_string = input(question)
# for i in range(5):
#     res = ''.join(random.sample(user_string[:], k=len(user_string)))
#     print(res, end="\n")

# task4
import random
random_int1 = random.randint(1, 100)
random_int2 = random.randint(1, 100)


def we_calculate():
    while True:
        try:
            user_input = int(input('What is ' + str(random_int1) +
                                   '+' + str(random_int2) + ' ?: '))
            corret_answer = random_int1+random_int2
            if user_input == "stop":
                break
        except ValueError:
            print("It is not valid answer! Please write an integer")
        else:
            if user_input != corret_answer:
                print('Your answer is NOT correct.Please try again.')
            else:
                print(f'Your answer {user_input} is correct.')
                break


we_calculate()
