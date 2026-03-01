# 16: Debugging & Best Practices

**Duration:** 40 minutes | **Difficulty:** Intermediate | **Key Skill:** Writing maintainable code

---

## ÌæØ What You'll Learn

- Debugging techniques (print, breakpoints)
- Writing readable code
- Comments and docstrings
- Testing your code

---

## Ì≥ö Debugging with print()

\`\`\`python
def process_data(data):
    print(f"Input: {data}")
    print(f"Type: {type(data)}")
    
    result = data * 2
    print(f"After processing: {result}")
    
    return result
\`\`\`

## Ì≥ö Good Code Practices

\`\`\`python
# ‚úÖ Good: Clear variable names, comments
def calculate_accuracy(predictions, actuals):
    """Calculate accuracy of predictions vs actual labels."""
    correct = sum(1 for p, a in zip(predictions, actuals) if p == a)
    accuracy = correct / len(actuals)
    return accuracy

# ‚ùå Bad: Confusing names, no doc
def calc(p, a):
    c = sum(1 for x, y in zip(p, a) if x == y)
    return c / len(a)
\`\`\`

---

## Ì¥ë Key Takeaways

‚úÖ Use print() to understand code flow
‚úÖ Write clear variable names
‚úÖ Document functions with docstrings
‚úÖ Test with simple examples first
‚úÖ  Use descriptive comments

---
