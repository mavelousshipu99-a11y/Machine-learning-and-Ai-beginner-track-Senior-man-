# 13: List Comprehensions - Pythonic Data Manipulation

**Duration:** 45 minutes | **Difficulty:** Intermediate | **Key Skill:** Pythonic code

---

## í¾¯ What You'll Learn

- Creating lists with comprehensions
- Filtering with conditions
- Nested comprehensions
- Dictionary and set comprehensions

---

## í³š Basic List Comprehension

\`\`\`python
# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension (more Pythonic)
squares = [i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]
\`\`\`

### With Conditions

\`\`\`python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]  # [2, 4, 6]

# Transform and filter
results = [x * 2 for x in range(10) if x % 2 == 0]
\`\`\`

### Dictionary & Set Comprehensions

\`\`\`python
# Dict comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ["cat", "dog", "bird"]}
# {3}
\`\`\`

---

## í·  ML Context

\`\`\`python
# Normalize dataset
raw_scores = [45, 78, 92, 65, 88]
max_score = max(raw_scores)
normalized = [s / max_score for s in raw_scores]
\`\`\`

---

## í´‘ Key Takeaways

âœ… List comprehensions are concise and fast
âœ… Syntax: [expression for item in iterable if condition]
âœ… Works for lists, dicts, sets
âœ… More readable than loops
âœ… Essential for ML data preprocessing

---
