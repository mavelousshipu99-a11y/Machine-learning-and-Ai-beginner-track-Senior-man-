# OOP Quick Reference

## Class Definition
\`\`\`python
class ClassName:
    def __init__(self, attr):
        self.attr = attr
\`\`\`

## Inheritance
\`\`\`python
class Child(Parent):
    def method(self):
        super().method()
\`\`\`

## Properties
\`\`\`python
@property
def value(self):
    return self._value
\`\`\`

## Common Patterns
- Single responsibility principle
- DRY (Don't Repeat Yourself)
- Composition over inheritance
