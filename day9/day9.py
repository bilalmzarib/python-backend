import time




def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
print("Closure Example - double(5):", double(5))  


def greet_decorator(func):
    def wrapper(name):
        print("Before function call")
        result = func(name)
        print("After function call")
        return result
    return wrapper

@greet_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Ali"))  




def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Execution time: {duration:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Finished slow function"

result = slow_function()

file_path = "results.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("=== Function Output Log ===\n")
    file.write(f"Closure Example Output: {double(5)}\n")
    file.write(f"Decorated say_hello Output: {say_hello('Ali')}\n")
    file.write(f"Slow Function Result: {result}\n")

print(f"Results saved to '{file_path}'")
