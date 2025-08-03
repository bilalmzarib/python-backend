import math
import random
import statistics
from custom_module import add

def is_positive(num):
    return num > 0

def square(num):
    return num * num


def mean(data):
    return statistics.mean(data)

def stdev(data):
    return statistics.stdev(data)


def format_float(num, digits=2):
    return f"{num:.{digits}f}"

data = [random.randint(1, 100) for _ in range(15)]

positive_data = list(filter(is_positive, data))


mean_val = mean(positive_data)
std_dev_val = stdev(positive_data)

formatted_mean = format_float(mean_val)
formatted_std_dev = format_float(std_dev_val)


print("Data:", data)
print("Positive data:", positive_data)
print(f"Mean: {formatted_mean}")
print(f"Standard Deviation: {formatted_std_dev}")

print(f"Square root of mean: {format_float(math.sqrt(mean_val))}")
print(add(5,6))