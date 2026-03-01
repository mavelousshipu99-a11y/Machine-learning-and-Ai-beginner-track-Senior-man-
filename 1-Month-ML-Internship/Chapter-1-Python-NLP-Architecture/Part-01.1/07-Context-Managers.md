# 07: Context Managers - Resource Management

**Duration:** 45 minutes | **Difficulty:** Intermediate | **Key Skill:** Resource cleanup

---

## í¾¯ What You'll Learn

- The with statement
- Creating context managers
- __enter__ and __exit__
- File handling best practices

---

## í³š Context Managers

### Using Context Managers

\`\`\`python
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed

database.close() # Not needed with context manager
\`\`\`

### Creating Context Managers

\`\`\`python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start:.2f}s")

with Timer():
    # Your code here
    pass
\`\`\`

---

## í´‘ Key Takeaways

âœ… with statement for resource management
âœ… Ensures cleanup even if errors occur
âœ… __enter__ and __exit__ methods
âœ… Best practice for ML data loading

---
