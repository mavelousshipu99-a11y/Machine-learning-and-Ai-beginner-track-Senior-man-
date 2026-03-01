# Advanced Solutions - Part 0

## Exercise 1: Text Analyzer Function

\`\`\`python
def analyze_text(text):
    words = text.lower().split()
    word_count = len(words)
    char_count = len(text)
    unique_words = len(set(words))
    
    return word_count, char_count, unique_words

text = "Python is awesome"
words, chars, unique = analyze_text(text)
print(f"Words: {words}, Chars: {chars}, Unique: {unique}")
\`\`\`

## Exercise 2: Data Pipeline

\`\`\`python
import statistics

def process_pipeline(data):
    # Calculate quartiles
    q1 = statistics.quantiles(data, n=4)[0]
    q3 = statistics.quantiles(data, n=4)[2]
    
    # Remove outliers
    filtered = [x for x in data if q1 <= x <= q3]
    
    # Normalize
    min_val = min(filtered)
    max_val = max(filtered)
    normalized = [(x - min_val)/(max_val - min_val) for x in filtered]
    
    return normalized

data = [1, 2, 3, 4, 5, 100, 200]
result = process_pipeline(data)
print(result)
\`\`\`

---
