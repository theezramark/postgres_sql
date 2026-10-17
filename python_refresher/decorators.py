# def add_stars(func):
#     def wrapper(*args, **kwargs):
#         print("*****")
#         result = func(*args, **kwargs)   
#         print("*****")
#         return result                    
#     return wrapper

# @add_stars
# def multiply(a, b):
#     """Multiply two numbers."""
#     return a * b

# print(multiply.__name__)
# print(multiply.__doc__)

# import functools
# import time

# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()          
#         result = func(*args, **kwargs)
#         end = time.perf_counter()            
#         print(f"{func.__name__} took {end - start:.2f} seconds")
#         return result
#     return wrapper

# @timer
# def slow_add(a, b):
#     time.sleep(1.5)       
#     return a + b

# print(slow_add(2, 3))

# import functools

# def announce(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Starting <function: {func.__name__}>")
#         return func(*args, **kwargs)
#     return wrapper

# @announce
# def multiply(a, b):
#      """Multiply two numbers."""
#      return a * b

# print(multiply(2,3))