# Part 3: Decision Trees & Random Forests - Exercises

**Difficulty:** Intermediate-Advanced | **Time:** 7-8 hours | **Capstone:** Movie Classifier

---

## 📝 Exercise Set 1: Information Theory

### Exercise 1.1: Calculate Entropy
Implement entropy calculation:
- Handle edge cases (all one class)
- Visualize entropy vs class distribution
- Show maximum entropy point

**File:** `entropy_calculation.py`

```python
def entropy(y):
    """Calculate Shannon entropy"""
    # H(S) = -sum(p_i * log2(p_i))
    pass

# Test: Pure set vs impure set
print(entropy([0, 0, 0, 0]))        # 0 (pure)
print(entropy([0, 0, 0, 1]))        # 0.811
print(entropy([0, 0, 1, 1]))        # 1.0 (max)
```

---

### Exercise 1.2: Information Gain
Implement information gain:
- Compare splits on different features
- Find split with maximum gain
- Visualize gain for all possible splits

**File:** `information_gain.py`

```python
def information_gain(parent, left, right):
    """IG = H(parent) - weighted H(children)"""
    pass

# Test: Find best split for feature
X_feature = [2, 4, 3, 5, 1, 6]
y = [0, 1, 0, 1, 0, 1]

gains = []
for threshold in X_feature:
    left_mask = X_feature <= threshold
    right_mask = ~left_mask
    gain = information_gain(y, y[left_mask], y[right_mask])
    gains.append((threshold, gain))
```

---

### Exercise 1.3: Gini Impurity (Optional)
Implement Gini impurity (alternative to entropy):
- $\text{Gini} = 1 - \sum p_i^2$
- Compare with entropy
- Show they rank splits similarly

**File:** `gini_impurity.py`

---

## 📝 Exercise Set 2: Decision Trees

### Exercise 2.1: Manual Tree Building
Build tree step-by-step:
- Start with root (whole dataset)
- Find best split at each node
- Grow tree manually
- Verify entropy/gain calculations

**File:** `manual_tree_building.py`

---

### Exercise 2.2: Implement Decision Tree
Create `DecisionTree` class:
- Build tree recursively
- Track splits and thresholds
- Implement predictions
- Handle edge cases

**File:** `decision_tree.py`

```python
class DecisionTree:
    def __init__(self, max_depth=5):
        pass
    
    def fit(self, X, y):
        # Build tree recursively
        pass
    
    def predict(self, X):
        # Traverse tree for predictions
        pass
    
    def _build_tree(self, X, y, depth=0):
        # Recursive tree building
        pass
```

---

### Exercise 2.3: Visualize Tree
Create tree visualization:
- Show nodes with split info
- Show leaf values
- Use graphviz or matplotlib

**File:** `visualize_tree.py`

---

## 📝 Exercise Set 3: Tree Pruning

### Exercise 3.1: Overfitting Demonstration
Show overfitting:
- Train unpruned tree
- Train pruned tree
- Plot train vs test accuracy
- Compare complexity

**File:** `tree_overfitting.py`

---

### Exercise 3.2: Cost Complexity Pruning
Implement pruning:
- Calculate complexity cost
- Remove nodes that don't improve test performance
- Find optimal alpha parameter

**File:** `cost_complexity_pruning.py`

```python
def prune_tree(node, alpha=0.01):
    """Remove branches that don't justify complexity"""
    pass
```

---

### Exercise 3.3: Validation Curve
Create validation curve:
- Varying max_depth parameter
- Plot train & test accuracy
- Find sweet spot

**File:** `validation_curve_tree.py`

---

## 📝 Exercise Set 4: Random Forests

### Exercise 4.1: Bootstrap Sampling
Implement bootstrap:
- Draw samples with replacement
- Same size as original
- Analyze diversity of bootstrap samples

**File:** `bootstrap_sampling.py`

```python
def bootstrap_sample(X, y):
    """Draw random sample with replacement"""
    indices = np.random.choice(len(X), len(X), replace=True)
    return X[indices], y[indices]
```

---

### Exercise 4.2: Random Forest Classifier
Implement `RandomForest`:
- Train multiple trees on bootstrap samples
- Combine predictions (majority vote)
- Compare single tree vs forest

**File:** `random_forest.py`

---

### Exercise 4.3: Feature Importance
Calculate feature importance:
- Count feature usage in splits
- Normalize across forest
- Visualize top features

**File:** `feature_importance.py`

```python
def feature_importance(forest, n_features):
    """Calculate which features are most important"""
    pass

# Visualize
important_features = feature_importance(forest, X.shape[1])
plt.barh(range(len(important_features)), important_features)
```

---

## 📝 Exercise Set 5: Iris & Real Data

### Exercise 5.1: Decision Tree on Iris
Build tree for Iris:
- Load Iris dataset
- Train decision tree
- Visualize tree
- Calculate accuracy

**File:** `iris_decision_tree.py`

---

### Exercise 5.2: Random Forest on Iris
Build forest for Iris:
- Train 10-tree forest
- Compare forest vs single tree
- Show feature importance
- Calculate out-of-bag error (OOB)

**File:** `iris_random_forest.py`

```python
# Out-of-bag error: test on samples not in bootstrap
# Better generalization estimate than cross-validation
```

---

### Exercise 5.3: Scikit-learn Comparison
Compare with sklearn:
- Train `DecisionTreeClassifier` from sklearn
- Compare with your implementation
- Verify same predictions
- Show performance match

**File:** `sklearn_comparison_tree.py`

---

## 🎯 Capstone: Movie Classifier

### Project: Build Complete Tree-Based Classifier

**Scenario:**
Classify movies as "Watch Now" or "Skip" based on features (rating, genre, runtime, year, etc.)

**Deliverables:**

#### Part 1: Explore Data (`part1_explore.py`)
- Load movie dataset (or create synthetic)
- Analyze features (numerical & categorical)
- Check class distribution
- Identify feature types

#### Part 2: Preprocess (`part2_preprocess.py`)
- Handle missing values
- Encode categorical features
- Split numerical features into bins (optional)
- Train/test split with stratification

#### Part 3: Build Tree Model (`part3_build_tree.py`)
```python
class MovieDecisionTree:
    def __init__(self, max_depth=5):
        pass
    
    def fit(self, X, y):
        pass
    
    def predict(self, X):
        pass
    
    def evaluate(self, y_true, y_pred):
        pass
```

#### Part 4: Build Forest Model (`part4_build_forest.py`)
```python
class MovieRandomForest:
    def __init__(self, n_trees=10, max_depth=5):
        pass
    
    def fit(self, X, y):
        # Train multiple trees
        pass
    
    def predict(self, X):
        # Majority vote
        pass
```

#### Part 5: Compare & Evaluate (`part5_compare.py`)
- Train single tree
- Train forest
- Compare metrics
- Show feature importance
- Visualize tree

#### Part 6: SciKit-learn Comparison (`part6_sklearn_comparison.py`)
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Train both your implementation and sklearn
# Compare predictions
# Compare metrics
# Verify match
```

#### Part 7: Report (`part7_report.py`)
```
TREE-BASED MOVIE CLASSIFIER REPORT
==================================

Dataset: 500 movies, 10 features
Target: Watch Now (1) vs Skip (0)
Distribution: 60% Watch, 40% Skip

Model 1: Single Decision Tree (max_depth=5)
  Training Accuracy: 0.92
  Testing Accuracy: 0.85
  Precision: 0.83
  Recall: 0.87
  F1 Score: 0.85

Model 2: Random Forest (10 trees, max_depth=5)
  Training Accuracy: 0.88
  Testing Accuracy: 0.86
  Precision: 0.85
  Recall: 0.85
  F1 Score: 0.85

Top 5 Important Features:
  1. Rating (0.32)
  2. Runtime (0.24)
  3. IMDb Score (0.18)
  4. Year (0.15)
  5. Genre (0.11)

Analysis:
- Forest: Slightly better generalization (0.86 vs 0.85)
- Tree: Less complex, easier to interpret
- Rating is most predictive feature
- No overfitting, train-test similar

Recommendation:
- Use forest for production
- Single tree acceptable for interpretability
```

**Success Criteria:**
- [ ] Data exploration complete
- [ ] Preprocessing handles all feature types
- [ ] Decision tree builds correctly
- [ ] Random forest trains and predicts
- [ ] Metrics calculated properly
- [ ] Matches scikit-learn results
- [ ] Feature importance visualized
- [ ] Report generated

---

## 🔗 Navigation

**[← Back to Part 3 Module](./Part-3-Decision-Trees.md)** | **[Chapter 3 →](../README.md)**
