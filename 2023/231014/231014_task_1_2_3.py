# # # Task 1 

# def countwords(sentance):
#     dic = {}
#     for item in sentance.split():
#         if item in dic:
#             dic[item] += 1
#         else:
#             dic[item] = 1

#     return print(sorted(dic.items()))

# user_string = input('Please write the sentance:')
# countwords(user_string)

# # task 2
# # adding the values with common key
# stock = {
# "banana": 6,
# "apple": 0,
# "orange": 32,
# "pear": 15
# }
# prices = {
# "banana": 4,
# "apple": 2,
# "orange": 1.5,
# "pear": 3
# }
# for key in stock:
#     if key in prices:
#         stock[key] = stock[key] * prices[key]
#         result = sum(stock.values())
#     else:
#         pass

# print(f'We have on stock: {stock}')
# print(f'The total price of stock is {result}')

# task 3
comp_list = [(x, x**2) for x in range(10)]
print(comp_list)
