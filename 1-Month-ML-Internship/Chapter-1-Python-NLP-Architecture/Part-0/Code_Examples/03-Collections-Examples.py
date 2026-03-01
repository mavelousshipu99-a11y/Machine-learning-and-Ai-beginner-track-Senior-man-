# Lists, Dicts, Tuples Examples

# LISTS
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
print(fruits[0])  # 'apple'
print(fruits[-1])  # 'orange'

# DICTIONARIES
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"])  # 'Alice'
person["age"] = 31
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 31, 'NYC'])

# TUPLES (immutable)
coordinates = (10, 20)
x, y = coordinates  # Unpacking
print(x, y)  # 10 20

# SETS (unique values)
numbers = {1, 2, 3, 3, 2, 1}
print(numbers)  # {1, 2, 3}
numbers.add(4)
print(4 in numbers)  # True
