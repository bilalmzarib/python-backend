def multiplier_generator(base):
    def multiplier(n):
        if base == 0:
            return n * n
        return n * base
    return multiplier

doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)

print("Doubler (5):", doubler(5))
print("Tripler (4):", tripler(4))
print("Squarer (6):", squarer(6))

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"[Call #{wrapper.calls}] Calling function '{func.__name__}'")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def greet(name):
    return f"Hello, {name}!"

print(greet("Ali"))
print(greet("Sara"))
print(greet("Mona"))
print("Total calls to 'greet':", greet.calls)

def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Invalid input: {arg} is not a positive number.")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print("Area (3 x 4):", calculate_area(3, 4))
