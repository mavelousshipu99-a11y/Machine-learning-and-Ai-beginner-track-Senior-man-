# Beginner Solutions - Part 0

## Exercise 1: Profile Creator

\`\`\`python
name = "Alice"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is student: {is_student}, Type: {type(is_student)}")
\`\`\`

## Exercise 2: Type Challenge

\`\`\`python
a = "10"
b = 10
c = 10.0

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>

# Can't add a + b (str + int)
# Can add b + c (int + float = float)
result = b + c  # 20.0
\`\`\`

## Exercise 3: Conversion

\`\`\`python
age_str = input("Enter your age: ")
age = int(age_str)
future_age = age + 10
print(f"In 10 years, you will be {future_age}")
\`\`\`

## Exercise 4: Text Processing

\`\`\`python
text = "  Hello, World! HELLO  "

text = text.strip()
print(text)  # "Hello, World! HELLO"

text = text.lower()
print(text)  # "hello, world! hello"

count = text.count("hello")
print(count)  # 2

text = text.replace("world", "python")
print(text)  # "hello, python! hello"
\`\`\`

---
