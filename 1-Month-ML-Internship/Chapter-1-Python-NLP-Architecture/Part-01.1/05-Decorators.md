# 05: Decorators - Function Enhancement

**Duration:** 60 minutes | **Difficulty:** Advanced | **Key Skill:** Metaprogramming

---

## í¾¯ What You'll Learn

- Creating decorators
- Decorator syntax (@)
- Decorators with parameters
- Real-world applications

---

## í³š Decorators

### Simple Decorator

\`\`\`python
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.2f}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)

slow_function()
\`\`\`

### ML Context

\`\`\`python
def validate_input(func):
    def wrapper(X, y):
        assert X.shape[0] == y.shape[0]
        return func(X, y)
    return wrapper

@validate_input
def train_model(X, y):
    pass
\`\`\`

---

## í´‘ Key Takeaways

âœ… Decorators modify function behavior
âœ… Used for logging, timing, validation
âœ… Critical in ML frameworks
âœ… Powerful metaprogramming tool

---
