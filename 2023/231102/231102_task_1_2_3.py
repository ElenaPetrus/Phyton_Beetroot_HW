#  Task 1
def abc():
    x = 1
    y = 2
    str1 = "resource"
    print("Python Exercises")


print(abc.__code__.co_nlocals)

#  Task 2


def make_multiplier(value: int | float):
    def inner(x: int | float):
        return x * value

    return inner


x10 = make_multiplier(10)
x2 = make_multiplier(2)

print("Static functions:")
print(f"10 * 2 = {x2(10)}")
print(f"10 * 10 = {x10(10)}")
print(f"5 * 10 = {x10(5)}")

#  Task 3


def choose_func(nums: list, func1, func2):
    if min(nums) > 0:
        return func1(nums)
    else:
        return func2(nums)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    #    squared_numbers = []
    # for num in nums:
    #     squared_numbers.append(num ** 2)
    # return squared_numbers
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
