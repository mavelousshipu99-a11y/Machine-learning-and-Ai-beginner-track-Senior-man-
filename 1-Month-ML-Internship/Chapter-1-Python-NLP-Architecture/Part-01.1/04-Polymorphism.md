# 04: Polymorphism - Flexible Design

**Duration:** 45 minutes | **Difficulty:** Intermediate | **Key Skill:** Flexible code

---

## í¾¯ What You'll Learn

- Method overriding
- Duck typing
- Abstract base classes
- Designing flexible APIs

---

## í³š Polymorphism Patterns

### Method Overriding

\`\`\`python
class Preprocessor:
    def process(self, data):
        pass

class TextPreprocessor(Preprocessor):
    def process(self, data):
        return data.lower().strip()

class NumericPreprocessor(Preprocessor):
    def process(self, data):
        return [float(x) for x in data]

def apply_pipeline(preprocessor, data):
    return preprocessor.process(data)
\`\`\`

---

## í´‘ Key Takeaways

âœ… Method overriding enables flexible code
âœ… Same method name, different implementation
âœ… Designed for extensibility
âœ… Critical for ML frameworks

---
