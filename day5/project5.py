
print("=== SET EXAMPLE ===")
items = ["apple", "banana", "apple", "orange", "banana"]
unique_items = set(items)
print("Original list:", items)
print("Unique items using set:", unique_items)


print("\n=== DICTIONARY: WORD FREQUENCY ===")
text = "this is a test this is only a test"
words = text.split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequencies:")
for word, count in word_freq.items():
    print(f"{word}: {count}")

print("\n=== MERGE DICTIONARIES USING WALRUS OPERATOR ===")

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "c": 4, "d": 6}
merged = {}

for key in dict1.keys() | dict2.keys():
    merged[key] = (
        (val := dict2.get(key)) if key not in dict1
        else (val := dict1[key] + dict2.get(key, 0))
    )

print("Merged dictionary (sum values on conflict):")
print(merged)
