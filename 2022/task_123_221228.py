# # Task 1 option 1
# import random
# random_int = random.sample(range(0, 50), 10)


# def the_lagest():

#     large = random_int[0]
#     for i in random_int:
#         if i > large:
#             large = i
#     return large

#     # # option 2
#     # return max(random_int)

# print(f'The lagest number is {the_lagest()}')


# # Task 2 option 1
# import random
# random_list1 = set(random.sample(range(0, 50), 10))
# random_list2 = set(random.sample(range(0, 50), 10))


# def common():
#     while True:
#         common_list = list(random_list2.intersection(random_list1))
#         if len(common_list) < 1:
#             print(f'There no common items in both lists')
#         else:
#             print(f'{common_list} are common for both lists')
#         break

# common()


# Task 3 option 1
import random
random_list = random.sample(range(0, 50), 30)


def filter():
    new_list = []
    for i in random_list:
        if (i % 7 == 0) and (i % 5 != 0):
            new_list.append(i)
    print(new_list)


filter()
