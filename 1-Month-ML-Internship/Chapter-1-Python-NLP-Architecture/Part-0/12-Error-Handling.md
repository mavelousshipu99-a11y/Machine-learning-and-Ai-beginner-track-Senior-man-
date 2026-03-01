# 12: Error Handling - Writing Robust Code

**Duration:** 45 minutes | **Difficulty:** Beginner | **Key Skill:** Defensive programming

---

## í¾¯ What You'll Learn

- Try-except blocks
- Handling specific exceptions
- Raising exceptions
- Finally clause

---

## í³š Try-Except

\`\`\`python
try:
    result = 10 / 0  # Will cause error
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    score = int("abc")  # Invalid conversion
except ValueError:
    print("Cannot convert string to int")
\`\`\`

### Multiple Exceptions

\`\`\`python
try:
    data = {"key": "value"}
    print(data["missing"])
except KeyError:
    print("Key not found")
except Exception as e:
    print(f"Unexpected error: {e}")
\`\`\`

### Finally

\`\`\`python
try:
    file = open("data.txt", "r")
    content = file.read()
finally:
    file.close()  # Runs no matter what
\`\`\`

---

## í·  ML Context

\`\`\`python
try:
    score = float(user_input)
    if score < 0 or score > 1:
        raise ValueError("Score must be 0-1")
except (ValueError, TypeError):
    print("Invalid score")
\`\`\`

---

## í´‘ Key Takeaways

âœ… try: runs risky code
âœ… except: handles errors
âœ… finally: cleanup code
âœ… raise: create custom errors
âœ… Robust code anticipates errors

---
