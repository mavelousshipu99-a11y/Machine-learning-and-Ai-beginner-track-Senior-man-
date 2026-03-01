# 14: Lambda Functions - Anonymous Functions

**Duration:** 40 minutes | **Difficulty:** Intermediate | **Key Skill:** Functional programming

---

## í¾¯ What You'll Learn

- Creating lambda functions
- Using with map(), filter(), sort()
- When to use lambdas
- Best practices

---

## í³š Basic Lambda

\`\`\`python
# Traditional function
def add(a, b):
    return a + b

# Lambda equivalent
add_lambda = lambda a, b: a + b

print(add_lambda(5, 3))  # 8
\`\`\`

### With map() and filter()

\`\`\`python
numbers = [1, 2, 3, 4, 5]

# Map: apply function to all
squared = list(map(lambda x: x**2, numbers))

# Filter: keep items where condition is True
evens = list(filter(lambda x: x % 2 == 0, numbers))
\`\`\`

### Sorting with Lambda

\`\`\`python
# Sort by second element
data = [(1, 3), (2, 1), (3, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
\`\`\`

---

## í·  ML Context

\`\`\`python
# Sort predictions by confidence
predictions = [(0.9, "cat"), (0.6, "dog"), (0.95, "bird")]
top_preds = sorted(predictions, key=lambda x: x[0], reverse=True)
\`\`\`

---

## í´‘ Key Takeaways

âœ… Lambda: anonymous one-line functions
âœ… Syntax: lambda args: expression
âœ… Great for simple transformations
âœ… Used with map, filter, sort, sorted
âœ… Keep lambdas simple and readable

---
