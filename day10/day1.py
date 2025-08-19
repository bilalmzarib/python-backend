
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("Custom Iterator (Countdown):")
for num in Countdown(5):
    print(num, end=' ')
print("\n")


def countdown_generator(start):
    while start > 0:
        yield start
        start -= 1

print("Generator (Countdown):")
for num in countdown_generator(5):
    print(num, end=' ')
print("\n")




squares = [x**2 for x in range(1, 6)]
print("List Comprehension (Squares):", squares)


squares_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension:", squares_dict)


even_set = {x for x in range(1, 11) if x % 2 == 0}
print("Set Comprehension (Even Numbers):", even_set)



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def infinite_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


print("\nFirst 10 Prime Numbers (using generator):")
prime_gen = infinite_primes()
for _ in range(10):
    print(next(prime_gen), end=' ')
