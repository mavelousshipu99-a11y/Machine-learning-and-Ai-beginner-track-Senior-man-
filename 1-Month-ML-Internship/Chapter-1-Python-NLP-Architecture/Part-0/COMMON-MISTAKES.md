# Common Mistakes in Part 0

Avoid these pitfalls!

## 1. Type Confusion

**❌ WRONG:**
\`\`\`python
age = "25"
future_age = age + 10  # ERROR!
\`\`\`

**✅ RIGHT:**
\`\`\`python
age = int("25")
future_age = age + 10  # 35
\`\`\`

## 2. List vs String

**❌ WRONG:**
\`\`\`python
text = "hello"
reversed_text = text[::-1]
reversed_text[0] = "o"  # ERROR! Strings are immutable
\`\`\`

**✅ RIGHT:**
\`\`\`python
text_list = list("hello")
text_list.reverse()
print("".join(text_list))  # "olleh"
\`\`\`

## 3. Dictionary Key Access

**❌ WRONG:**
\`\`\`python
data = {"name": "Alice"}
age = data["age"]  # KeyError!
\`\`\`

**✅ RIGHT:**
\`\`\`python
data = {"name": "Alice"}
age = data.get("age", "Unknown")  # "Unknown"
\`\`\`

## 4. Loop Variable Scope

**❌ WRONG:**
\`\`\`python
for i in range(5):
    x = i * 2

print(x)  # 8 (x still exists!)
# This can lead to bugs
\`\`\`

**✅ RIGHT:**
\`\`\`python
result = []
for i in range(5):
    result.append(i * 2)

print(result)  # [0, 2, 4, 6, 8]
\`\`\`

## 5. List Mutation in Loops

**❌ WRONG:**
\`\`\`python
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    if lst[i] > 2:
        lst.remove(lst[i])  # Can skip elements!
\`\`\`

**✅ RIGHT:**
\`\`\`python
lst = [1, 2, 3, 4, 5]
lst = [x for x in lst if x <= 2]
# Or use filter during iteration
\`\`\`

## 6. Indentation Errors

**❌ WRONG:**
\`\`\`python
if True:
print("Hello")  # ERROR! Indentation needed
\`\`\`

**✅ RIGHT:**
\`\`\`python
if True:
    print("Hello")
\`\`\`

---
