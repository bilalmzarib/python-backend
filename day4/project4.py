print("\n--- Lists ---")
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)
print("First fruit:", fruits[0])
print("Fruits from index 1:", fruits[1:])
fruits.append("date")
print("After adding 'date':", fruits)
fruits.sort()
print("Sorted fruits:", fruits)

print("\n--- List Comprehension ---")
squares = [x * x for x in range(10)]
print("Squares from 0 to 9:", squares)

print("\n--- Tuples ---")
point = (3, 4)
print("Point coordinates:", point)

def get_person_info():
    return ("Alice", 30)

name, age = get_person_info()
print("Name:", name)
print("Age:", age)

print("\n--- Union Operators ---")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
combined_set = set1 | set2
print("Combined set:", combined_set)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined_dict = dict1 | dict2
print("Combined dictionary:", combined_dict)

print("\n--- List and Tuple Practice ---")
numbers = [5, 3, 8, 6, 1]
print("Original numbers:", numbers)
numbers.sort()
print("Sorted numbers:", numbers)
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
numbers_tuple = tuple(numbers)
print("Numbers as tuple:", numbers_tuple)

print("\n--- Find Second Largest Number ---")

def second_largest_number(my_list):
    unique_list = list(set(my_list))
    if len(unique_list) < 2:
        return None
    unique_list.sort(reverse=True)
    return unique_list[1]

my_numbers = [10, 20, 4, 45, 99, 99]
print("My numbers:", my_numbers)
print("Second largest number:", second_largest_number(my_numbers))

print("\n--- Merge Two Dictionaries ---")
person1 = {"name": "Alice", "age": 25}
person2 = {"age": 30, "city": "Paris"}
merged_person = person1 | person2
print("Merged person info:", merged_person)
