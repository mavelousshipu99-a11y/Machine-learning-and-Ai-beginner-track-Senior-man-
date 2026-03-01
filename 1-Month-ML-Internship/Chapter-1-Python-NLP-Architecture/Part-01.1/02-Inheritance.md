# 02: Inheritance - Code Reuse Through Hierarchy

**Duration:** 50 minutes | **Difficulty:** Intermediate | **Key Skill:** OOP design

---

## í¾¯ What You'll Learn

- Creating parent and child classes
- Inheriting attributes and methods
- Overriding methods
- super() function
- Multiple inheritance basics

---

## í³š Core Concept: Inheritance

**Inheritance** allows a class to inherit properties from another class.

### Basic Inheritance

\`\`\`python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy barks!
\`\`\`

### Using super()

\`\`\`python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
\`\`\`

---

## í·  ML Context

\`\`\`python
class BaseClassifier:
    def __init__(self, learning_rate):
        self.lr = learning_rate

class NeuralNetwork(BaseClassifier):
    def __init__(self, learning_rate, layers):
        super().__init__(learning_rate)
        self.layers = layers
\`\`\`

---

## í´‘ Key Takeaways

âœ… Inheritance reduces code duplication
âœ… Child classes inherit parent methods
âœ… Override methods to customize behavior
âœ… super() calls parent methods
âœ… Essential for framework design

---
