# Variables & Types - Summary Sheet

**Variables** store data in memory with a name.

## Key Syntax
\`\`\`python
name = value          # Create variable
type(variable)        # Check type
int(), float(), str() # Convert types
\`\`\`

## The Three Mutable Types
- **int**: Whole numbers (5, -10, 0)
- **float**: Decimals (3.14, -0.5)
- **str**: Text ("hello", 'world')
- **bool**: True/False

## Common Pattern
\`\`\`python
# 1. Create
age = "25"

# 2. Check type
print(type(age))  # <class 'str'>

# 3. Convert if needed
age = int(age)

# 4. Use
new_age = age + 1
\`\`\`

---
