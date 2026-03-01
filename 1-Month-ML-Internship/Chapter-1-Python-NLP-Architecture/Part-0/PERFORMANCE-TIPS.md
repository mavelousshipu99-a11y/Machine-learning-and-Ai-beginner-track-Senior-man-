# Performance Tips - Part 0

## 1. List Comprehensions vs Loops

\`\`\`python
# Loops (slower)
result = []
for x in range(1000000):
    if x % 2 == 0:
        result.append(x * 2)

# List comprehension (faster)
result = [x * 2 for x in range(1000000) if x % 2 == 0]
\`\`\`

## 2. Use Built-ins Instead of Loops

\`\`\`python
# Slow
total = 0
for x in numbers:
    total += x

# Fast
total = sum(numbers)
\`\`\`

## 3. Avoid Repeated Lookups

\`\`\`python
# Slow
for i in range(len(long_list)):
    process(long_list[i])

# Fast
for item in long_list:
    process(item)
\`\`\`

## 4. Use join() Not Concatenation

\`\`\`python
# Slow
result = ""
for word in words:
    result += word + " "

# Fast
result = " ".join(words)
\`\`\`

---
