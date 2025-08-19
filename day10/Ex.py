

class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

print("Exercise 1: Fibonacci Sequence (First 10 terms):")
for num in FibonacciIterator(10):
    print(num, end=' ')
print("\n")


def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield sign * abs(num)
        sign *= -1

print("Exercise 2: Alternating Signs:")
nums = [3, 7, 1, 9, 2]
for n in alternating_signs(nums):
    print(n, end=' ')
print("\n")



words = ["hello", "world"]
ascii_dict = {
    word: {char: ord(char) for char in word}
    for word in words
}
print("Exercise 3: Word to Char ASCII Dictionary:")
print(ascii_dict)
print()



text = "The quick brown fox jumps over the lazy dog"
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = {char.upper() for char in text.lower() if char in vowels}
print("Exercise 4: Uppercase Vowels Found in String:")
print(found_vowels)
print()



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("Exercise 5: First 6 Prime Numbers:")
prime_gen = primes()
for _ in range(6):
    print(next(prime_gen), end=' ')
