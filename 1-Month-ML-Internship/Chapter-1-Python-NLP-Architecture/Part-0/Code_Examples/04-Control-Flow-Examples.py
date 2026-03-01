# If/Else and Loops Examples

# Conditionals
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# FOR LOOP
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate through list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# With index
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# WHILE LOOP
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# Break and Continue
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i == 2:
        continue  # Skip this iteration
    print(i)
