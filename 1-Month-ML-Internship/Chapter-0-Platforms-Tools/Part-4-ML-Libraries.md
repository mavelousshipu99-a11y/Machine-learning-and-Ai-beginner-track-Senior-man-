# Part 4: ML Libraries Overview

**Duration:** 2-3 hours | **Level:** Beginner | **Prerequisites:** Part 1-3 (Python, Git, Jupyter/IDE)

---

## 📚 Overview

This course uses **specific libraries for different tasks**. Understanding what each does helps you:
- Know which tool to use for each problem
- Understand why we compare with libraries
- Learn professional ML workflows

This Part introduces the main libraries used in all 4 Chapters.

---

## 🎯 Learning Outcomes

By the end of this Part, you will:
- ✅ Understand NumPy and array operations
- ✅ Know Pandas for data manipulation
- ✅ Understand scikit-learn for ML algorithms
- ✅ Know Matplotlib and Seaborn for visualization
- ✅ Know when to use each library

---

## 🧮 Part 1: NumPy - Numerical Computing

### **What is NumPy?**

NumPy is the **foundation for numerical computing in Python**. It provides:
- **Arrays** (like lists, but faster)
- **Mathematical operations** (matrix multiplication, eigenvalues)
- **Random number generation**
- **Linear algebra functions**

### **Core Concept: Arrays**

```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Operations (element-wise)
arr * 2          # [2, 4, 6, 8, 10]
arr + 10         # [11, 12, 13, 14, 15]
np.sqrt(arr)     # [1.0, 1.41, 1.73, 2.0, 2.24]

# Matrix operations
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
np.dot(vector_a, vector_b)  # Dot product = 32

# Statistics
np.mean(arr)     # 3.0
np.std(arr)      # 1.414
```

### **Why NumPy?**

- **Fast:** Written in C, much faster than Python lists
- **Convenient:** Mathematical operations on entire arrays
- **Foundation:** Used by pandas, scikit-learn, matplotlib

### **Key NumPy Functions Used in Course**

```python
np.array()              # Create arrays
np.shape, np.reshape()  # Array dimensions
np.dot(), np.matmul()   # Matrix multiplication
np.mean(), np.std()     # Statistics
np.linalg.eig()         # Eigenvalues/vectors
np.random.randn()       # Random numbers
np.linspace()           # Create sequences
```

### **Resources:**
- **NumPy Official Docs:** [numpy.org/doc](https://numpy.org/doc/)
- **NumPy Tutorial:** [Real Python NumPy](https://realpython.com/numpy-tutorial/)
- **NumPy Cheat Sheet:** [NumPy Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)

---

## 📊 Part 2: Pandas - Data Manipulation

### **What is Pandas?**

Pandas provides **DataFrames** - like Excel spreadsheets but for Python.

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [95, 87, 92]
})

# View data
df.head()          # First few rows
df.describe()      # Statistics

# Access columns
df['Name']         # Column
df.loc[0]          # Row
df['Score'].mean() # Average score

# Filter
high_scores = df[df['Score'] > 90]

# Operations
df['Grade'] = df['Score'].apply(lambda x: 'A' if x > 90 else 'B')
```

### **Why Pandas?**

- **Intuitive:** Like Excel but programmable
- **Data cleaning:** Handle missing values, duplicates
- **Grouping:** Aggregate and transform data
- **I/O:** Read/write CSV, Excel, JSON, SQL

### **Key Pandas Functions Used in Course**

```python
pd.read_csv()           # Load CSV files
df.head(), df.tail()    # View data
df.describe()           # Statistics
df.groupby()            # Grouping operations
df.fillna()             # Handle missing values
df['col'].apply()       # Transform columns
df.to_csv()             # Save data
```

### **Resources:**
- **Pandas Official Docs:** [pandas.pydata.org](https://pandas.pydata.org/)
- **Pandas Tutorial:** [Real Python Pandas](https://realpython.com/learning-paths/pandas-data-science/)
- **10 Minutes to Pandas:** [pandas.pydata.org/getting-started](https://pandas.pydata.org/getting-started/)

---

## 🤖 Part 3: Scikit-learn - Machine Learning

### **What is Scikit-learn?**

Scikit-learn provides **ready-made ML algorithms** we'll compare against our from-scratch implementations.

```python
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris

# Load data
X, y = load_iris(return_X_y=True)

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Evaluate
score = model.score(X, y)  # R² score
```

### **Algorithms Covered:**

| Algorithm | Module | Usage |
|-----------|--------|-------|
| Linear Regression | `linear_model` | Part 1, Chapter 3 |
| Logistic Regression | `linear_model` | Part 2, Chapter 3 |
| Decision Trees | `tree` | Part 3, Chapter 3 |
| Random Forests | `ensemble` | Part 3, Chapter 3 |
| PCA | `decomposition` | Part 4, Chapter 3 |
| K-Means | `cluster` | Data clustering |

### **Why Compare with Scikit-learn?**

1. **Validate** - Check if your implementation is correct
2. **Performance** - See how fast optimized code is
3. **Professional** - Learn industry-standard libraries
4. **Scale** - Handle larger datasets with optimized code

### **Key Scikit-learn Pattern**

```python
# All models follow same pattern:
model = ModelClass(parameters)
model.fit(X_train, y_train)         # Train
predictions = model.predict(X_test) # Predict
score = model.score(X_test, y_test) # Evaluate
```

### **Resources:**
- **Scikit-learn Official Docs:** [scikit-learn.org](https://scikit-learn.org/)
- **Machine Learning with Scikit-learn:** [Real Python](https://realpython.com/train-test-split-and-cross-validation-in-python/)
- **Scikit-learn Cheat Sheet:** [Scikit-learn Cheat Sheet](https://github.com/rougier/scikit-learn-cheatsheet)

---

## 📈 Part 4: Matplotlib & Seaborn - Visualization

### **Matplotlib - Basic Plotting**

```python
import matplotlib.pyplot as plt
import numpy as np

# Create figure and plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Function')
plt.legend()
plt.grid()
plt.show()

# Save figure
plt.savefig('sine_plot.png', dpi=300)
```

### **Seaborn - Statistical Visualization**

```python
import seaborn as sns
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Histograms
sns.histplot(df['Age'], kde=True)

# Scatter plots
sns.scatterplot(x='Age', y='Score', data=df, hue='Group')

# Correlation heatmap
sns.heatmap(df.corr(), annot=True)

plt.show()
```

### **Visualization Use Cases:**

| Plot Type | Use Case | Library |
|-----------|----------|---------|
| Line plot | Trends over time | Matplotlib |
| Scatter plot | Relationships between variables | Matplotlib/Seaborn |
| Histogram | Distribution of single variable | Seaborn |
| Box plot | Comparing distributions | Seaborn |
| Heatmap | Correlations, confusion matrix | Seaborn |
| Pie chart | Proportions | Matplotlib |

### **Why Visualization Matters**

1. **Understand Data** - See patterns humans can't in tables
2. **Debug** - Visualize your model's errors
3. **Communicate** - Show results to others
4. **Explore** - Discover insights in data

### **Resources:**
- **Matplotlib Official Guide:** [matplotlib.org/stable/users/index](https://matplotlib.org/stable/users/index.html)
- **Seaborn Tutorial:** [seaborn.pydata.org/tutorial](https://seaborn.pydata.org/tutorial.html)
- **Python Plotting for Exploratory Data Analysis:** [Real Python](https://realpython.com/plotting-with-matplotlib/)

---

## 🎯 Part 5: Library Comparison & Use Cases

### **Chapter 1: Python & NLP**
- **NumPy** - Store text as numerical vectors
- **Regular expressions** - Text cleaning (built-in `re`)
- Custom implementations - Embeddings, similarity

### **Chapter 2: Data & Search**
- **Pandas** - Load and explore CSV/JSON data
- **Matplotlib/Seaborn** - Exploratory Data Analysis
- Custom implementations - Indexing, ranking

### **Chapter 3: ML Algorithms**
- **NumPy** - Mathematical operations
- **Custom code** - Algorithms from scratch
- **scikit-learn** - Compare against library versions
- **Matplotlib** - Visualize models

### **Chapter 4: Capstone**
- **All libraries** above
- **Streamlit** (optional) - Web interfaces
- Professional code organization

---

## 📦 Complete Installation Check

Verify all libraries are installed:

```python
import numpy
import pandas
import matplotlib
import seaborn
import sklearn

print("✅ NumPy:", numpy.__version__)
print("✅ Pandas:", pandas.__version__)
print("✅ Matplotlib:", matplotlib.__version__)
print("✅ Seaborn:", seaborn.__version__)
print("✅ Scikit-learn:", sklearn.__version__)
print("\n🎉 All libraries ready!")
```

---

## 🔗 Additional Resources

### **NumPy:**
- **NumPy Getting Started:** [numpy.org/learn](https://numpy.org/learn/)
- **100 NumPy Exercises:** [GitHub - 100 NumPy Exercises](https://github.com/rougier/numpy-100)

### **Pandas:**
- **Pandas Getting Started:** [pandas.pydata.org/getting-started.html](https://pandas.pydata.org/getting-started.html)
- **Pandas Cookbook:** [Real Python Pandas Cookbook](https://realpython.com/pandas-cookbook/)

### **Scikit-learn:**
- **Scikit-learn Tutorial:** [scikit-learn.org/stable/tutorial/](https://scikit-learn.org/stable/tutorial/)
- **Hands-on ML Book:** [hands-on-ml.com](https://hands-on-ml.com/) (excellent reference)

### **Visualization:**
- **Matplotlib Gallery:** [matplotlib.org/stable/gallery/index](https://matplotlib.org/stable/gallery/index.html)
- **Seaborn Gallery:** [seaborn.pydata.org/examples](https://seaborn.pydata.org/examples.html)

### **Combined ML Stack:**
- **Machine Learning Mastery:** [machinelearningmastery.com](https://machinelearningmastery.com/)
  - Tutorials for NumPy, Pandas, Scikit-learn together
- **Introduction to NumPy and Pandas:** [Real Python](https://realpython.com/learning-paths/data-science-python/)

---

## ✅ Success Criteria

You've successfully completed Part 4 when:

- [ ] All libraries installed and working
- [ ] Can create and manipulate NumPy arrays
- [ ] Can load and explore data with Pandas
- [ ] Can train models with scikit-learn
- [ ] Can create visualizations with Matplotlib/Seaborn
- [ ] Understand use cases for each library
- [ ] Know when library versions match your implementations

---

## 🎓 Next Steps

Once you've completed this Part:
→ Move to **Part 5: Data & Resources** to understand where to get datasets

---

**Part Status:** ✅ Complete  
**Difficulty:** ⭐⭐ (Beginner-Intermediate)  
**Time Estimate:** 2-3 hours  
**Key Takeaway:** Understanding your tools is as important as understanding algorithms. Libraries amplify good code; bad understanding of libraries leads to bad code.
