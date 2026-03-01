# 11: Itertools - Advanced Iteration Tools

**Duration:** 50 minutes | **Difficulty:** Advanced | **Key Skill:** Functional iteration

---

## í¾¯ What You'll Learn

- chain, combinations, permutations
- groupby and compress
- cycle and repeat
- Practical applications

---

## í³š Itertools

### Combinations and Permutations

\`\`\`python
from itertools import combinations, permutations

items = ['a', 'b', 'c']
combos = list(combinations(items, 2))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
\`\`\`

### groupby

\`\`\`python
from itertools import groupby

data = [(1, 'a'), (1, 'b'), (2, 'c')]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
\`\`\`

---

## í´‘ Key Takeaways

âœ… Efficient iteration tools
âœ… Memory-friendly implementations
âœ… Composable functions
âœ… Functional programming style

---
