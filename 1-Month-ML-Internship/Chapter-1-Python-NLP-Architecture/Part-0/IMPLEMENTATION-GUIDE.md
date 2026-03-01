# Implementation Guide - Part 0

## How to Implement Concepts from Scratch

### 1. Implement Your Own String Methods

\`\`\`python
def my_upper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

print(my_upper("hello"))  # HELLO
\`\`\`

###2. Implement list.sort()

\`\`\`python
def my_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
\`\`\`

### 3. Implement min() and max()

\`\`\`python
def my_min(lst):
    smallest = lst[0]
    for item in lst[1:]:
        if item < smallest:
            smallest = item
    return smallest

def my_max(lst):
    largest = lst[0]
    for item in lst[1:]:
        if item > largest:
            largest = item
    return largest
\`\`\`

---
