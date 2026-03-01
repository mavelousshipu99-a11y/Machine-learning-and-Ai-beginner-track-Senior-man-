# 03-Functions-Solutions.py - SOLUTIONS

import math
import string

# Solution 1: Circle Area
def circle_area(radius):
    return math.pi * radius ** 2

print(f"Circle area (r=5): {circle_area(5):.2f}")

# Solution 2: Clean Text
def clean_text(text):
    text = text.strip().lower()
    return text.translate(str.maketrans('', '', string.punctuation))

print(clean_text("  HELLO WORLD!!!  "))

# Solution 3: Normalize List
def normalize_list(values):
    min_val = min(values)
    max_val = max(values)
    return [(x - min_val) / (max_val - min_val) for x in values]

print(normalize_list([10, 20, 30, 40]))

# Solution 4: Email Validation
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

print(is_valid_email("user@example.com"))
