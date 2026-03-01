# 12: Functional Programming - Advanced Patterns

**Duration:** 50 minutes | **Difficulty:** Advanced | **Key Skill:** FP paradigm

---

## í¾¯ What You'll Learn

- Map, filter, reduce functions
- First-class functions
- Immutability concepts
- Functional ML pipelines

---

## í³š Functional Programming

### Map and Filter

\`\`\`python
# Traditional
doubled = [x * 2 for x in [1, 2, 3]]

# Functional
doubled = list(map(lambda x: x * 2, [1, 2, 3]))

# Filter
evens = list(filter(lambda x: x % 2 == 0, [1,2,3,4]))
\`\`\`

### Reduce

\`\`\`python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
\`\`\`

---

## í´‘ Key Takeaways

âœ… Map, filter, reduce patterns
âœ… Pure functions and immutability
âœ… Composable data processing
âœ… ML pipeline design

---
