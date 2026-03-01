# ML Context Guide - Part 0

How Python fundamentals apply to Machine Learning

## Data Representation

### Strings
- **Raw text input** - User reviews, tweets, articles
- **Labels** - "positive", "negative", "spam", "ham"
- **Categorical features** - Colors, categories, classes

### Lists
- **Feature vectors** - [age, salary, experience]
- **Training data** - Multiple samples as list of lists
- **Predictions** - Output array from model

\`\`\`python
# ML Example
training_samples = [
    [25, 50000, 3],  # person 1: age, salary, experience  
    [30, 60000, 5],  # person 2
]
\`\`\`

### Dictionaries
- **Configurations** - Model hyperparameters
- **Labeled data** - {image_id: label}
- **Results** - {metric: value}

\`\`\`python
# ML Example
model_config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 100
}
\`\`\`

### NumPy Arrays
- **Matrices** - Feature matrix (m x n)
- **Vectors** - Weight vectors in neural networks
- **Feature engineering** - Efficient transformations

\`\`\`python
import numpy as np
X = np.array([[1, 2], [3, 4]])  # Feature matrix
y = np.array([0, 1])             # Labels
X_normalized = (X - X.mean()) / X.std()  # Normalization
\`\`\`

## Control Flow in ML

### Conditionals
- **Data validation** - Check if values in valid range
- **Early stopping** - Stop training if loss improves

\`\`\`python
if loss < best_loss:
    best_loss = loss
    save_model()
\`\`\`

### Loops
- **Training loop** - Iterate over epochs
- **Data processing** - Iterate over samples
- **Cross-validation** - Iterate over folds

\`\`\`python
for epoch in range(100):
    for batch in training_data:
        predictions = model.predict(batch)
        loss = calculate_loss(predictions, batch.labels)
\`\`\`

## Functions for ML

- **Modular preprocessing** - Reusable data cleaning
- **Model evaluation** - Computing metrics
- **Feature engineering** - Creating new features

\`\`\`python
def normalize(data, min_val, max_val):
    return (data - min_val) / (max_val - min_val)

def calculate_accuracy(y_true, y_pred):
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)
\`\`\`

---
