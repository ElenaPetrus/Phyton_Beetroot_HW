
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

# s = 'h i d'
# print(s.replace(' ', ''))

# define a function that takes a single positional argument - an integer

# then, let's define a second function inside the first one
# the second (inner) function should take a single positional parameter as well

# and return a multiple of the outer parameter and the one provided to this inner one


# and run the outer one and then the inner one
# few times with different parameter provided to outer one and inner one
# def outer_func(fist_out_arg):
#     def inner_func(fist_in_arg):
#     inner_func(outer_func(fist_out_arg))
# outer_func()

# class OlenaClass:
#  pass
# def olena_func(param_one):
#  return param_one()
# class Person:
#      def __init__(self, name, age):
#        self.name = name
#       self.age = age
# print(Person.name)
# person_1.our_oun_fucnctiom("Linus", 36)
# person_1 = Person("Linus", 36)
# print(person_1.name)


# # create your own class called "Animal"
# class Animal:
#     # create a method __init__ that is going to take 3 parameters except 'self': color, kind, number of legs
#     def __init__(self, name, size, character, preferences):
#         # assign these parameters to "self" line by line
#         self.name = name
#         self.size = size
#         self.character = character
#         self.preferences = preferences
#         # create another method inside "Animal", "print_information"

#     # def print_information(self):
#     #     print(
#     #         f"hi, I'm an {self.size} and {self.character} {self.name}, I like {self.preferences}")

#         def __str__(self):
#             return f"hi, I am an {self.size} and {self.character} {self.name}, I like {self.preferences}"


# # create (instantiate) two animals
# animal1 = Animal("Zebra", "big", "serious", "grass")
# animal2 = Animal("Monkey", "small", "cheerful", "bananas")
# # animal1run your method to print information on both of them
# # animal1.print_information()
# # animal2.print_information()
# print(animal1)
# print(animal2)


# import time
# snowflake_loop = '\\|/ —'


# for _ in range(25):
#     for i in snowflake_loop:
#         print(i, end='')
#         time.sleep(0.5)
#         print('\r', end='')


# # def decorator(some_funct):
# #     print("beginning_message")
# #     some_funct()
# #     print("ending_message")
# #     return some_funct
# # # @decorator syntax is equal to the second last line of code
# # @decorator
# # def say_hi():
# #     print("Hi")
# # say_hi = decorator(say_hi)  # this one is equal to @decorator
# # say_hi()
# # we can modify the above mentioned
# def decorator(some_funct):
#     def wrapper():
#         print("beginning_message")
#         some_funct()
#         print("ending_message")
#     return wrapper

# # @decorator syntax is equal to the second last line of code

# @decorator
# def say_hi():
#     print("Hi")


# say_hi = decorator(say_hi)  # this one is equal to @decorator
# say_hi()


# class MyClass:

# @staticmethod
# def some_method():
#     print("this method does nothing with self")


# def our_decorator(some_funct):
#     def wrapper(*args):
#         print("something actually meaningful that we want to do before the function")
#         some_funct(*args)
#         print("something actually meaningful that we want to do after the function")
#     return wrapper


# @our_decorator
# def some_function_that_takes_two_parameters(first_param, second_param):
#     print(second_param)


# some_function_that_takes_two_parameters(5)

# create a "Mammal" class
# assign some general attributes to it
# create a sub-class (Human or something) and put some sublass-specific attribute(s) into it
# create an instance of a sub-class and print the attributes


class Mammal:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def __str__(self):
        class_name = self.__class__.__name__
        modifier = "an" if any([class_name.startswith(letter)
                               for letter in "AEIOU"]) else "a"
        return f"I'm {modifier} {class_name}, my gender is {self.gender} and age is {self.age}"


class Human(Mammal):
    def __init__(self, iq, *args):
        Mammal.__init__(self, *args)
        self.iq = iq


class Animal(Mammal):
    pass


human = Human(180, "male", 5)
mammal = Mammal("female", 10)
animal = Animal("female", 13)
print(human)
print(mammal)
print(animal)
