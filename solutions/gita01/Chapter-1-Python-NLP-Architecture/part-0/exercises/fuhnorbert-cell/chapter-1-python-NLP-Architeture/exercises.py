name = "Alice"          
age = 25               
height = 1.68            
is_student = True        

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

a = "10"
b = 10
c = 10.0
print(type(a))
print(type(b))
print(type(c))

# Read user's age as string
age_str = input("Enter your age: ")

# Convert string to integer
age_int = int(age_str)

# Add 10 years
future_age = age_int + 10

# Print result
print("In 10 years, you will be", future_age, "years old.")

text = " Hello, World! HELLO "

# 1. Remove whitespace (from beginning and end)
text = text.strip()

# 2. Convert to lowercase
text = text.lower()

# 3. Count how many times "hello" appears
count_hello = text.count("hello")

# 4. Replace "world" with "python"
text = text.replace("world", "python")

print("Processed text:", text)
print("Number of 'hello':", count_hello)

filename = "document.pdf"

# Find file extension using slicing
extension = filename[filename.index(".") + 1:]

print("File extension:", extension)

email = input("Enter email: ")

if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")