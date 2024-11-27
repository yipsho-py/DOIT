############  დავალება 1 #########

# def positive_check(func):
#     def wrapper(number):
#         if number < 0:
#             raise ValueError("The number must be positive!")
#         result = func(number)
#         print(f"The result is: {result}")
#         return result
#     return wrapper

# @positive_check
# def return_number(number):
#     return number

# try:
#     return_number(5)
# except ValueError as e:
#     print(e)

# try:
#     return_number(-3)
# except ValueError as e:
#     print(e)



############  დავალება 2 ############



# def positive_check(func):
#     return lambda number: (func(number) if number >= 0 else raise ValueError("The number must be positive!"))

# def return_number(number):
#     return number

# return_number = positive_check(return_number)

# try:
#     return_number(5)
# except ValueError as e:
#     print(e)

# try:
#     return_number(-3)
# except ValueError as e:
#     print(e)




############  დავალება 3 ############


# import time

# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function '{func.__name__}' executed in {end_time - start_time} seconds.")
#         return result
#     return wrapper

# @time_decorator
# def sample_function():
#     time.sleep(2)

# sample_function()


############  დავალება 4 ############


# class LoggingMeta(type):
#     def __new__(cls, name, bases, dct):
#         print(f"Creating class: {name}")
#         methods = [key for key, value in dct.items() if callable(value)]
#         print(f"Methods in {name}: {methods}")
#         return super().__new__(cls, name, bases, dct)

# class MyClass(metaclass=LoggingMeta):
#     def method_one(self):
#         pass
    
#     def method_two(self):
#         pass

# class AnotherClass(metaclass=LoggingMeta):
#     def hello(self):
#         pass

# MyClass()
# AnotherClass()



