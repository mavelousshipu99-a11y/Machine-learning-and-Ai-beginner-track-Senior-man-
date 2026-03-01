# Intermediate Solutions - Part 0

## Exercise 1: List Operations

\`\`\`python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

max_val = max(numbers)  # 9
min_val = min(numbers)  # 1

count_ones = numbers.count(1)  # 2

numbers = [x for x in numbers if x != 1]
print(numbers)  # [2, 3, 4, 5, 6, 9]

average = sum(numbers) / len(numbers)
print(average)  # 5.166...
\`\`\`

## Exercise 5: Frequency Counter

\`\`\`python
text = "the quick brown fox"
words = text.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)  # {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1}
\`\`\`

## Exercise 7: Grade Classifier

\`\`\`python
grade = int(input("Enter grade (0-100): "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
\`\`\`

---
