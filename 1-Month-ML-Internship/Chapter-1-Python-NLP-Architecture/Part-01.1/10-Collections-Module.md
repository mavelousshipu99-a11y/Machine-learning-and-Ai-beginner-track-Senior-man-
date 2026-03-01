# 10: Collections Module - Specialized Data Structures

**Duration:** 50 minutes | **Difficulty:** Intermediate | **Key Skill:** Data structures

---

## í¾¯ What You'll Learn

- Counter for counting items
- defaultdict for grouping
- namedtuple for structured data
- deque for efficient queues

---

## í³š Collections

### Counter

\`\`\`python
from collections import Counter

data = ['a', 'b', 'a', 'c', 'b', 'a']
counter = Counter(data)
print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})
print(counter.most_common(2))  # [('a', 3), ('b', 2)]
\`\`\`

### defaultdict

\`\`\`python
from collections import defaultdict

word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1
\`\`\`

---

## í´‘ Key Takeaways

âœ… Counter for frequency analysis
âœ… defaultdict prevents KeyError
âœ… namedtuple for clarity
âœ… Improves code efficiency

---
