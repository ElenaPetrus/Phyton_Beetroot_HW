# from typing import List, Tuple

# # We assume that all lists passed to functions are same length N


# # answers
# # 1 - n
# # 2 - 1
# # 3 - n^2
# # 4 - n
# # 5 - n^2
# # 6 - log n


# def question1(first_list: List[int], second_list: List[int]) -> List[int]:
#     res: List[int] = []
#     for el_first_list in first_list:
#         if el_second_list in second_list:
#             res.append(el_first_list)
#     return res


# def question2(n: int) -> int:
#     for _ in range(10):
#         n **= 3
#     return n


# def question3(first_list: List[int], second_list: List[int]) -> List[int]:
#     temp: List[int] = first_list[:]
#     for el_second_list in second_list:
#         flag = False
#         for check in temp:
#             if second_list == check:
#                 flag = True
#                 break
#         if not flag:
#             temp.append(second_list)
#     return temp


# def question4(input_list: List[int]) -> int:
#     res: int = 0
#     for el in input_list:
#         if el > res:
#             res = el
#     return res


# question1([1, 2, 3, 4], [5, 6, 7, 8])
# # question2()
# # question3()
# # question4()

# i = 2
# n = 8


# for j in range(2, n+1):
#     if i >= n:
#         break
#     print("Hello World !!!")
#     i *= i


# # # This code is contributed by akashish__
# # # explain why the above code has the complexity O(log(log(n)))
# Складність алгоритму наведеного вище коду можна проаналізувати таким чином:
# Цикл повторює j від 2 до n, тому цикл буде виконано n - 1 разів.
# Оператор if перевіряє, чи є i більше або дорівнює n. Якщо i більше або дорівнює n, цикл припиняється.
# Інструкція print буде виконуватися один раз під час кожної ітерації циклу.
# Оператор i *= i множить значення i на себе та присвоює результат i. Це означає, що i буде зведено в квадрат під час кожної ітерації циклу.
# Отже, ми бачимо, що значення i буде зводитися в квадрат під час кожної ітерації циклу. Тому значення i буде 2**2, 2**4, 2**8, 2**16 і так далі, поки i не стане більшим або дорівнює n.
# Кількість ітерацій, необхідних для того, щоб i стало більше або дорівнює n, можна обчислити, розв’язавши таке рівняння:
# 2**(2**k) >= n
# Це рівняння можна переписати так:
# 2**k >= log2(n)
# Логарифмування обох сторін дає:
# k >= log2(log2(n))
# Отже, кількість ітерацій, необхідних для того, щоб i стало більше або дорівнює n, дорівнює O(log log n).
# Оскільки оператор print виконується один раз під час кожної ітерації циклу, часова складність усього коду становить O(log log n).
