# def allow_only_for_people_not_robots(some_function):
#     def inner(*args, **kwargs):
#         if args[0].type != "robot":
#             return some_function(*args, **kwargs)
#         else:
#             print(f'{args[0].name} is not a person')
#     return inner


# class Base:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     @staticmethod
#     def who_am_i():
#         return "I am a person"

#     @classmethod
#     def which_class_am_i(cls):
#         return type(cls)

#     @allow_only_for_people_not_robots
#     def return_the_first_name(self):
#         return self.first_name

#     @allow_only_for_people_not_robots
#     def return_the_second_name(self):
#         return self.second_name

#     @allow_only_for_people_not_robots
#     def do_some_other_stuff(self):
#         print("hi")


# class Person(Base):
#     def __init__(self, *args):
#         Base.__init__(self, *args)
#         self.type = "person"


# class Robot(Base):
#     def __init__(self, *args):
#         Base.__init__(self, *args)
#         self.type = "robot"


# person_1 = Person("Peter", "Smith")
# person_2 = Person("John", "Doe")
# person_3 = Person("Julia", "Olsson")

# print(person_1.return_the_first_name())
# print(person_2.return_the_first_name())
# print(person_3.return_the_first_name())

# print(person_1.who_am_i())
# print(person_2.who_am_i())
# print(person_3.who_am_i())

# print(person_1.which_class_am_i())
# print(person_2.which_class_am_i())
# print(person_3.which_class_am_i())

# robot_1 = Robot("Android", "IOS")
# print(robot_1.who_am_i())

def print_function(n, text):
    if n == 0:
        print('I cannot print more')
    else:
        print(f'{text}')
        return print_function(n-1, text)


print_function(5, 'cat')
