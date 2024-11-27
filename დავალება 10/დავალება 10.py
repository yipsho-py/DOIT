########## დავალება 1 ##########

# def group_elements(list1, list2):
#     return [str(item) for item in zip(list1, list2)]

# # მაგალითი
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# result = group_elements(list1, list2)
# print(result)


########## დავალება 2 ##########

# get_even_numbers = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

# numbers = [1, 2, 3, 4, 5, 6, 7]
# result = get_even_numbers(numbers)
# print(result)


########## დავალება 3 ##########


# from functools import filter

# get_positive_numbers = lambda lst: list(filter(lambda x: x > 0, lst))

# numbers = [-10, -5, 0, 5, 10]
# result = get_positive_numbers(numbers)
# print(result)


########## დავალება 4 ##########


# from functools import filter

# is_palindrome = lambda lst: list(filter(lambda x: x == x[::-1], lst))

# strings = ["racecar", "hello", "madam", "world", "level"]
# result = is_palindrome(strings)
# print(result)

########## დავალება 5 ##########


# from functools import reduce

# def product_of_elements(lst):
#     try:
#         if not all(isinstance(i, (int, float)) for i in lst):
#             raise TypeError("ყველა ელემენტი უნდა იყოს რიცხვი.")
#         return reduce(lambda x, y: x * y, lst)
#     except TypeError as e:
#         return str(e)

# # მაგალითი
# numbers = [1, 2, 3, 4, 5]
# result = product_of_elements(numbers)
# print(result)


########## დავალება 6 ##########

# def filter_ending_strings(lst, ending):
#     try:
#         if not all(isinstance(i, str) for i in lst) or not isinstance(ending, str):
#             raise TypeError("პარამეტრები უნდა იყოს სტრიქონები.")
#         return list(filter(lambda x: x.endswith(ending), lst))
#     except TypeError as e:
#         return str(e)

# # მაგალითი
# strings = ['hello', 'world', 'coding', 'nod']
# ending = 'ing'
# result = filter_ending_strings(strings, ending)
# print(result)



