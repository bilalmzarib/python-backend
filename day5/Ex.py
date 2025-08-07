
print("== Exercise 1: Sets ==")


numbers = [3, 5, 7, 5, 9, 3]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)
print("Union (A ∪ B):", A | B)
print("Intersection (A ∩ B):", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference (A Δ B):", A ^ B)


text = "apple banana apple cherry banana"
words = text.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))


print("\n== Exercise 2: Dictionaries ==")

student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}
print("Student dictionary:", student)


text = "hello world hello"
word_list = text.split()
word_count = {}

for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:", word_count)


squares = {x: x**2 for x in range(1, 6)}
print("Squares (1 to 5):", squares)


print("\n== Exercise 3: Walrus Operator (Input Validation) ==")

while (num := int(input("Enter a number greater than 10: "))) <= 10:
    print("Try again...")

print("You entered:", num)


print("\n== Exercise 4: Merge Dictionaries with Conflict Resolution ==")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {}

for key in dict1.keys() | dict2.keys():
    if key in dict1 and key in dict2:
        merged[f"{key}_resolved"] = dict1[key] + dict2[key]
    else:
        merged[key] = dict1.get(key) or dict2.get(key)

print("Merged dictionary with resolution:", merged)
