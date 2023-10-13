# # Task 1
# import random

# correct_number = random.randint(1, 10)
# print('Let\'s play the guessing game!')

# while True:
#     guess = input("Try to guess the number between 1 and 10. Type a digit: ")

#     if not guess.isdigit():
#         print("Don't confuse me. Please enter a digit.")
#     else:
#         guess = int(guess)
#         if guess < correct_number:
#             print("Please go a bit higher.")
#         elif guess > correct_number:
#             print("Please go a bit lower.")
#         else:
#             print("You are the MINDREADER!!!")
#             break


# # Task 2
# while True:
#     name = input("Enter your name: ")
#     current_age = (input("Enter your age: "))

#     if not current_age.isdigit():
#         print("Don't confuse me. Please enter a digit.")
#     else:
#         current_age = int(current_age)
#         if current_age > 130:
#             print("Are you sure? You're an ancient artefact. ")
#         else:
#             future_age = current_age+1
#             print(
#                 f"Hello {name}, on your next birthday you’ll be {future_age} years")
#             break

#  task3
import random
question = 'Please type any word: '
user_string = input(question)
for i in range(5):
    # In each iteration of the loop, a random permutation of the user_string is generated.
    # random.sample() to select a random sample of characters from user_string, ensuring that no character is repeated.
    # ''.join(...) to join these characters into a string.
    res = ''.join(random.sample(user_string[:], k=len(user_string)))
    print(res, end='\n')
