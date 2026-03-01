# 02: Strings - Text Processing for ML & NLP

**Duration:** 45 minutes | **Difficulty:** Beginner | **Key Skill:** Text manipulation fundamentals

---

## 🎯 What You'll Learn

- Creating and using strings
- Accessing string characters
- String methods for text cleaning
- String formatting
- ML Context: Essential for all NLP tasks

---

## 📚 Core Concept: Working with Strings

Strings are sequences of characters used to represent text. In machine learning, especially NLP, you'll spend significant time manipulating strings for data preprocessing.

### Creating Strings

```python
# Single quotes
greeting = 'Hello'

# Double quotes (more common)
greeting = "Hello"

# Triple quotes (multi-line)
paragraph = """The quick brown fox
jumps over the lazy dog.
Multiple lines are possible."""

# Empty string
empty = ""

# String with special characters
path = "C:\\Users\\Data\\file.txt"  # Use \\ for backslash
special = "Line 1\nLine 2"        # \n for newline
tab_text = "Name\tAge"            # \t for tab
```

---

## 🔍 String Indexing & Slicing

Since strings are sequences, you can access individual characters:

```python
text = "Python"

# Indexing (getting single character)
print(text[0])      # "P" (first character)
print(text[1])      # "y"
print(text[-1])     # "n" (last character)
print(text[-2])     # "o" (second from end)

# Slicing (getting substrings)
print(text[0:3])    # "Pyt" (characters 0, 1, 2)
print(text[1:4])    # "yth"
print(text[2:])     # "thon" (from index 2 to end)
print(text[:3])     # "Pyt" (from start to index 3)
print(text[::2])    # "Pto" (every 2nd character)
print(text[::-1])   # "nohtyP" (reversed!)

# Common pattern: Get file extension
filename = "document.pdf"
extension = filename[-4:]  # Last 4 characters: ".pdf"
extension = filename.split('.')[-1]  # "pdf"
```

---

## 🛠️ Essential String Methods (ML-Focused)

### Cleaning Methods (Critical for Data Preprocessing)

```python
# Remove whitespace (very common in data cleaning)
text = "  Hello World  \n"
print(text.strip())         # "Hello World" (removes leading/trailing)
print(text.lstrip())        # "Hello World  \n" (remove left only)
print(text.rstrip())        # "  Hello World" (remove right only)

# Case conversion
email = "John.Smith@Gmail.COM"
email.lower()               # "john.smith@gmail.com"
email.upper()               # "JOHN.SMITH@GMAIL.COM"
email.capitalize()          # "John.smith@gmail.com" (first letter cap)

# Replace (text normalization)
text = "I love apples and apples are great"
text.replace("apples", "oranges")  # Replace all occurrences
# "I love oranges and oranges are great"

text.replace("apples", "oranges", 1)  # Replace only first
# "I love oranges and apples are great"

# Find & Count
text = "Hello World"
print(text.find("o"))       # 4 (index of first "o")
print(text.count("l"))      # 3 (count of "l")

# Split (tokenization - key for NLP!)
text = "The quick brown fox"
words = text.split()        # ['The', 'quick', 'brown', 'fox']

text = "apple,banana,orange"
fruits = text.split(",")    # ['apple', 'banana', 'orange']

# Join (opposite of split - combine words)
words = ["cats", "dogs", "birds"]
sentence = " ".join(words)  # "cats dogs birds"
csv_line = ",".join(words)  # "cats,dogs,birds"
```

---

## 📝 String Formatting (Displaying Data)

### Method 1: Concatenation (Simple)

```python
name = "Alice"
age = 25
message = "My name is " + name + " and I'm " + str(age) + " years old"
print(message)
# Output: "My name is Alice and I'm 25 years old"
```

### Method 2: f-strings (Recommended - Pythonic!)

```python
name = "Alice"
age = 25
gpa = 3.85

# Simple substitution
print(f"My name is {name}")  # "My name is Alice"

# Expressions in braces
print(f"I will be {age + 1} next year")  # "I will be 26 next year"

# Format floating point
print(f"My GPA is {gpa:.2f}")  # "My GPA is 3.85" (2 decimal places)

# Padding
print(f"ID: {100:05d}")  # "ID: 00100" (pad to 5 digits with zeros)
```

### Method 3: .format() (Older style, still useful)

```python
name = "Bob"
score = 92.5

message = "Hello {}, your score is {:.1f}".format(name, score)
print(message)  # "Hello Bob, your score is 92.5"
```

---

## 🔤 String Checking Methods

```python
text = "Hello123"

# Checking content
text.isalpha()              # False (has numbers)
text.isdigit()              # False (has letters)
text.isalnum()              # True (only letters/numbers)

"123".isdigit()             # True
"Hello".isalpha()           # True
" ".isspace()               # True

# Check if contains
"@" in "email@example.com"  # True
"xyz" in "Hello"            # False

# Check start/end
text = "document.pdf"
text.startswith("doc")      # True
text.endswith(".pdf")       # True
```

---

## ⚠️ Common String Pitfalls

### Pitfall 1: Strings Are Immutable

```python
text = "hello"
# You CANNOT change a character directly!
# text[0] = "H"  # ❌ ERROR!

# Instead, create a new string
text = text.upper()  # ✅ Correct
print(text)  # "HELLO"
```

### Pitfall 2: Forgetting Whitespace

```python
text = "Hello"
print(len(text))              # 5

# Extra spaces matter!
text_with_space = "Hello "
print(len(text_with_space))   # 6

# Solution: Strip when needed
user_input = input("Enter name: ")  # User might type " Bob " with spaces
user_input = user_input.strip()     # Remove the spaces
```

### Pitfall 3: Mixing Data Types

```python
name = "Alice"
age = 25

# ❌ This won't work
# message = "My name is " + name + " and I'm " + age

# ✅ Use f-strings or convert
message = f"My name is {name} and I'm {age}"
# OR
message = "My name is " + name + " and I'm " + str(age)
```

---

## 🧠 ML Context: String Processing for NLP

### Text Cleaning Pipeline

```python
# Raw text from user input or document
raw_text = "  The QUICK brown fox!!!  "

# Step 1: Strip whitespace
cleaned = raw_text.strip()

# Step 2: Convert to lowercase (normalization)
cleaned = cleaned.lower()

# Step 3: Remove punctuation (often needed)
import string
cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))

# Result: "the quick brown fox"
# Now ready for tokenization and analysis!
```

### Tokenization (Breaking text into words)

```python
text = "Machine learning is awesome!"

# Simple word tokenization
words = text.lower().split()
# ['machine', 'learning', 'is', 'awesome!']

# With punctuation removal
import string
text_clean = text.translate(str.maketrans('', '', string.punctuation)).lower()
words = text_clean.split()
# ['machine', 'learning', 'is', 'awesome']
```

---

## 📝 Exercises

### Try It! (Quick Checks)

**Exercise 2.1: Indexing & Slicing**
```python
word = "algorithm"
print(word[0])      # What do you get?
print(word[-1])     # What do you get?
print(word[3:6])    # What do you get?
print(word[::-1])   # What do you get?
```

**Exercise 2.2: String Methods**
```python
# Use string methods to:
text = "  Welcome to Python  "
# 1. Remove whitespace
# 2. Convert to uppercase
# 3. Find the index of 'P'
# 4. Count how many times 'o' appears
```

**Exercise 2.3: String Formatting**
```python
name = "Charlie"
score = 88.5

# Use f-string to print:
# "Charlie scored 88.50 out of 100"
```

### Do It! (Hands-on Practice)

**Exercise 2.4: Email Validation Check**
```python
email = "  User@Gmail.COM  "

# 1. Strip whitespace
# 2. Convert to lowercase
# 3. Check if "@" is in the email
# 4. Check if it ends with ".com"
# 5. Print: "Email is valid" or "Email is invalid"
```

**Exercise 2.5: Text Statistics**
```python
text = "Python programming is fun and powerful"

# 1. Find total number of characters
# 2. Count words (split by space)
# 3. Count how many times "a" appears
# 4. Find the first occurrence of "and"
# 5. Print statistics in a nice format
```

### Master It! (Challenges)

**Exercise 2.6: Text Cleaning Function**
```python
# Create a text processing pipeline:
raw_text = "   The QUICK brown FOX!!!   "

# Task:
# 1. Strip whitespace
# 2. Convert to lowercase
# 3. Replace multiple spaces with single space
# 4. Remove exclamation marks
# Expected result: "the quick brown fox"

# (Hint: Look up replace() method)
```

**Exercise 2.7: Data Formatter**
```python
# You have training data that needs formatting:
student_name = "john doe"
student_id = 12345
test_score = 92.333333

# Format as:
# "Student: John Doe (ID: 12345)"
# "Score: 92.33 / 100"

# Requirements:
# - Capitalize name properly
# - Format score to 2 decimal places
```

---

## 🎬 Code-Along Example: Tweet Analysis

```python
# Simulating tweet analysis (common NLP task)

tweet = "  I LOVE Python!!! It's so AMAZING!!!  "

# Processing steps
print("Original tweet:")
print(f"'{tweet}'")
print()

# Step 1: Clean whitespace
cleaned = tweet.strip()
print(f"After strip: '{cleaned}'")
print()

# Step 2: Lowercase for normalization
normalized = cleaned.lower()
print(f"After lowercase: '{normalized}'")
print()

# Step 3: Statistics
word_count = len(normalized.split())
char_count = len(normalized)
exclamation_count = normalized.count("!")

print(f"Word count: {word_count}")
print(f"Character count: {char_count}")
print(f"Exclamation marks: {exclamation_count}")
print()

# Step 4: Extract sentiment indicators
has_love = "love" in normalized
has_amazing = "amazing" in normalized
print(f"Contains 'love': {has_love}")
print(f"Contains 'amazing': {has_amazing}")
```

Output:
```
Original tweet:
'  I LOVE Python!!! It's so AMAZING!!!  '

After strip: 'I LOVE Python!!! It's so AMAZING!!!'

After lowercase: 'i love python!!! it's so amazing!!!'

Word count: 6
Character count: 36
Exclamation marks: 6

Contains 'love': True
Contains 'amazing': True
```

---

## 🔑 Key Takeaways

✅ Strings are sequences of characters (indexed starting at 0)  
✅ Access characters with indexing and slicing  
✅ Use string methods for data cleaning (.strip(), .lower(), .replace())  
✅ Split for tokenization, join to reconstruct  
✅ f-strings are the modern way to format output  
✅ Strings are immutable (can't change in place)  

---

## 🚀 Next: [03-Numbers & Math](./03-Numbers-Math.md)

Learn numerical operations essential for ML algorithms!

---

## 📚 Additional Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [String Formatting](https://realpython.com/python-f-strings/)
