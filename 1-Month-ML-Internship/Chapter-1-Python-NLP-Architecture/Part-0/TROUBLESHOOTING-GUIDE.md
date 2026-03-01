# Troubleshooting Guide

## Common Errors & Fixes

### "NameError: name 'x' is not defined"
**Cause:** Variable used before creation or typo
**Fix:** Define variable first, check spelling
\`\`\`python
# Wrong
print(x)
x = 5

# Right
x = 5
print(x)
\`\`\`

### "IndexError: list index out of range"
**Cause:** Trying to access index that doesn't exist
**Fix:** Use len() to check size, remember 0-indexing
\`\`\`python
lst = [1, 2, 3]
print(lst[0])  # OK - 0 exists
print(lst[5])  # ERROR - only 0,1,2 exist
print(lst[-1]) # OK - last element
\`\`\`

### "KeyError: 'name'"
**Cause:** Dictionary key doesn't exist
**Fix:** Use .get() or check first
\`\`\`python
d = {"age": 30}
print(d["name"])        # ERROR
print(d.get("name"))     # OK - returns None
\`\`\`

### "TypeError: can only concatenate str (not 'int') to str"
**Cause:** Mixing types
**Fix:** Convert explicitly
\`\`\`python
name = "Alice"
age = 30
print(name + str(age))  # Right
print(f"{name}{age}")   # Also right
\`\`\`

### "IndentationError: expected an indented block"
**Cause:** Missing or wrong indentation
**Fix:** Use consistent indentation (4 spaces)
\`\`\`python
if x > 5:
    print("bigger")      # 4 spaces indented
else:
    print("smaller")     # 4 spaces indented
\`\`\`

---

## Debugging Checklist
1. Read error message carefully
2. Check line number in error
3. Look for typos
4. Verify variable definitions
5. Add print() statements
6. Search FAQ and COMMON-MISTAKES
7. Check provided examples

---
