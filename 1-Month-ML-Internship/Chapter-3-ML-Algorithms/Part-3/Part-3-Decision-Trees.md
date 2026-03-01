# Part 3: Decision Trees & Random Forests - Module

## 🎯 Learning Objectives

By the end of this part, you will:
- Understand information gain and entropy
- Build decision trees from scratch using splits
- Implement ID3/CART decision tree algorithm
- Learn tree pruning to prevent overfitting
- Build random forests by ensemble learning
- Understand feature importance
- Apply to real classification problems

---

## 1. Decision Tree Fundamentals

### 1.1 What Are Decision Trees?

A decision tree is a flowchart-like model that makes predictions by:
1. Starting at the root
2. Asking questions about features
3. Following branches based on answers
4. Reaching leaf nodes (predictions)

**Example: Iris Classification**
```
             Is sepal length > 5.8?
           /                        \
         Yes                         No
         /                            \
  Is petal width > 1.65?        Classification: Setosa
    /             \
  Yes              No
  /                \
Virginica        Versicolor
```

### 1.2 Advantages & Disadvantages

**Advantages:**
- Interpretable (explains decisions)
- Handles non-linear relationships
- No feature scaling needed
- Handles categorical features naturally
- Fast predictions

**Disadvantages:**
- Prone to overfitting
- Unstable (small changes → big changes)
- Biased toward dominant classes
- Can miss linear patterns

---

## 2. Information Theory Basics

### 2.1 Entropy

**Entropy** measures uncertainty/impurity in a set.

$$H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

Where:
- $S$: set of samples
- $c$: number of classes
- $p_i$: proportion of class $i$

**Interpretation:**
- $H = 0$: Pure (all same class)
- $H = 1$: Maximum confusion (equal classes)

**Examples:**
- All class 0: $H = 0$ (pure)
- 50% class 0, 50% class 1: $H = 1$ (maximum impurity)
- 75% class 0, 25% class 1: $H = -0.75\log(0.75) - 0.25\log(0.25) = 0.811$

### 2.2 Information Gain

**Information Gain** measures reduction in entropy from a split.

$$IG(S, A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$$

Where:
- $S$: original set
- $A$: attribute (feature)
- $S_v$: subset where $A = v$

**Algorithm:** Choose split with maximum information gain!

### 2.3 Information Gain Implementation

```python
def entropy(y):
    """Calculate Shannon entropy"""
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))

def information_gain(parent, left_child, right_child):
    """Calculate information gain from split"""
    n = len(parent)
    n_left = len(left_child)
    n_right = len(right_child)
    
    # Weighted entropy of children
    child_entropy = (n_left / n) * entropy(left_child) + \
                    (n_right / n) * entropy(right_child)
    
    # Information gain
    return entropy(parent) - child_entropy
```

---

## 3. Building Decision Trees

### 3.1 Decision Tree Node

```python
class Node:
    """Node in decision tree"""
    
    def __init__(self, feature=None, threshold=None, 
                 left=None, right=None, value=None):
        # For decision nodes:
        self.feature = feature          # Feature index to split on
        self.threshold = threshold      # Split threshold
        self.left = left                # Left subtree (feature <= threshold)
        self.right = right              # Right subtree (feature > threshold)
        
        # For leaf nodes:
        self.value = value              # Class prediction
```

### 3.2 Decision Tree Building Algorithm

```python
class DecisionTree:
    """Decision tree classifier (CART algorithm)"""
    
    def __init__(self, max_depth=None, min_samples_split=2, random_state=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None
        self.random_state = random_state
    
    def fit(self, X, y):
        """Build decision tree recursively"""
        if self.random_state is not None:
            np.random.seed(self.random_state)
        
        self.tree = self._build_tree(X, y, depth=0)
        return self
    
    def _build_tree(self, X, y, depth=0):
        """Recursively build tree"""
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))
        
        # Stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or \
           n_samples < self.min_samples_split or \
           n_classes == 1:
            # Create leaf node
            leaf_value = self._most_common_class(y)
            return Node(value=leaf_value)
        
        # Find best split
        best_gain = 0
        best_feature = None
        best_threshold = None
        
        for feature_idx in range(n_features):
            feature_values = X[:, feature_idx]
            thresholds = np.unique(feature_values)
            
            for threshold in thresholds:
                # Split on this feature and threshold
                left_mask = feature_values <= threshold
                right_mask = ~left_mask
                
                # Skip if split doesn't separate
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue
                
                # Calculate information gain
                gain = information_gain(
                    y,
                    y[left_mask],
                    y[right_mask]
                )
                
                # Keep best split
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_idx
                    best_threshold = threshold
        
        # If no split found, create leaf
        if best_feature is None:
            leaf_value = self._most_common_class(y)
            return Node(value=leaf_value)
        
        # Recursively build subtrees
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask
        
        left_subtree = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_subtree = self._build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return Node(feature=best_feature, 
                   threshold=best_threshold,
                   left=left_subtree, 
                   right=right_subtree)
    
    def predict(self, X):
        """Predict class for samples"""
        return np.array([self._traverse_tree(x, self.tree) for x in X])
    
    def _traverse_tree(self, x, node):
        """Traverse tree to make prediction"""
        if node.value is not None:
            # Leaf node
            return node.value
        
        # Decision node
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        else:
            return self._traverse_tree(x, node.right)
    
    @staticmethod
    def _most_common_class(y):
        """Return most frequent class"""
        classes, counts = np.unique(y, return_counts=True)
        return classes[np.argmax(counts)]
```

---

## 4. Tree Pruning

### 4.1 Why Prune?

Trees grown to maximum depth overfit:
- Perfect training accuracy
- Poor test accuracy
- Memorizes noise

**Pruning** removes branches that don't improve test performance.

### 4.2 Cost Complexity Pruning

```python
def prune_tree(node, alpha=0.01):
    """
    Post-pruning using cost complexity
    alpha: complexity parameter (higher = more pruning)
    """
    if node is None:
        return node
    
    # Recursively prune subtrees
    if node.left is not None:
        node.left = prune_tree(node.left, alpha)
    if node.right is not None:
        node.right = prune_tree(node.right, alpha)
    
    # If both children are leaves, consider pruning
    if (node.left is not None and node.left.value is not None and 
        node.right is not None and node.right.value is not None):
        
        # Calculate cost of keeping vs removing split
        # (Simplified - real implementation calculates prediction error)
        # Prune if both children are leaves
        if np.random.random() < alpha:
            majority_class = node.left.value  # Could be improved
            node.value = majority_class
            node.left = None
            node.right = None
    
    return node
```

---

## 5. Random Forests

### 5.1 Ensemble Learning Concept

**Ensemble:** Combine multiple weak learners into strong learner.

**Idea:** Train many trees, average predictions.

- Individual trees: High variance, low bias
- Forest average: Low variance, low bias

### 5.2 Random Forest Algorithm

```python
class RandomForest:
    """Random forest classifier"""
    
    def __init__(self, n_trees=10, max_depth=10, 
                 min_samples_split=2, random_state=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.random_state = random_state
        self.trees = []
    
    def fit(self, X, y):
        """Train random forest"""
        if self.random_state is not None:
            np.random.seed(self.random_state)
        
        for i in range(self.n_trees):
            # Bootstrap sample
            indices = np.random.choice(len(X), len(X), replace=True)
            X_sample = X[indices]
            y_sample = y[indices]
            
            # Train tree on bootstrap sample
            tree = DecisionTree(max_depth=self.max_depth,
                              min_samples_split=self.min_samples_split)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
        
        return self
    
    def predict(self, X):
        """Predict using majority vote"""
        predictions = np.array([tree.predict(X) for tree in self.trees])
        
        # Majority vote
        return np.array([np.bincount(predictions[:, i]).argmax() 
                        for i in range(len(X))])
    
    def predict_proba(self, X):
        """Get probability estimates"""
        predictions = np.array([tree.predict(X) for tree in self.trees])
        
        # Fraction voting yes
        return np.mean(predictions, axis=0)
```

### 5.3 Feature Importance

Which features are most useful for splits?

```python
def feature_importance(trees, n_features):
    """Calculate feature importance from forest"""
    importance = np.zeros(n_features)
    
    for tree in trees:
        # Walk tree and count feature usage
        importance += _count_features(tree.tree, n_features)
    
    # Normalize
    return importance / np.sum(importance)

def _count_features(node, n_features):
    """Count feature usage in tree"""
    importance = np.zeros(n_features)
    
    if node.value is not None:
        # Leaf node
        return importance
    
    # Decision node: count this feature
    importance[node.feature] += 1
    
    # Recurse
    importance += _count_features(node.left, n_features)
    importance += _count_features(node.right, n_features)
    
    return importance
```

---

## 6. Handling Categorical Features

### 6.1 Pure Categorical Features

```python
def find_best_split_categorical(X, y, feature_idx):
    """Find best split for categorical feature"""
    feature_values = X[:, feature_idx]
    unique_values = np.unique(feature_values)
    
    best_gain = 0
    best_split = None
    
    for value in unique_values:
        # Split: feature == value vs feature != value
        left_mask = feature_values == value
        right_mask = ~left_mask
        
        if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
            continue
        
        gain = information_gain(y, y[left_mask], y[right_mask])
        
        if gain > best_gain:
            best_gain = gain
            best_split = value
    
    return best_split, best_gain
```

### 6.2 Mixed Categorical and Numerical

```python
def find_best_split_mixed(X, y, feature_idx, feature_type):
    """Find best split for feature (numerical or categorical)"""
    
    if feature_type == 'numerical':
        return find_best_split_numerical(X, y, feature_idx)
    else:  # categorical
        return find_best_split_categorical(X, y, feature_idx)
```

---

## 7. Advantages of Tree-Based Models

| Feature | Advantage |
|---------|-----------|
| Interpretability | Easy to visualize and explain |
| Non-linear | Captures complex patterns |
| No scaling | Raw feature values work |
| Mixed types | Handles categorical & numerical |
| Feature selection | Identifies important features |
| Speed | Fast prediction time |

---

## 📚 Key Formulas

$$\text{Entropy}(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

$$\text{Information Gain}(S, A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$$

$$\text{Gini Impurity} = 1 - \sum_{i=1}^{c} p_i^2$$

---

## � Additional Resources & Learning Links

### **Decision Tree Algorithms**
- [Decision Trees (Wikipedia)](https://en.wikipedia.org/wiki/Decision_tree) - Overview and theory
- [Information Gain and Entropy](https://en.wikipedia.org/wiki/Information_gain_in_decision_trees) - Mathematical foundations
- [ID3 and C4.5 Algorithms](https://en.wikipedia.org/wiki/ID3_algorithm) - Decision tree learning algorithms

### **Scikit-learn Decision Trees**
- [Decision Tree Classification](https://scikit-learn.org/stable/modules/tree.html) - Official documentation
- [DecisionTreeClassifier API](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) - Implementation details
- [Tree Visualization](https://scikit-learn.org/stable/modules/tree.html#tree-structure) - Visualizing tree structures

### **Random Forests & Ensemble Methods**
- [Random Forest (Wikipedia)](https://en.wikipedia.org/wiki/Random_forest) - Ensemble method theory
- [Ensemble Learning](https://en.wikipedia.org/wiki/Ensemble_learning) - Bootstrap aggregating principles
- [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) - API reference

### **Boosting Algorithms**
- [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting) - Boosting methodology
- [XGBoost Documentation](https://xgboost.readthedocs.io/) - Production-grade gradient boosting
- [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost) - Adaptive boosting algorithm

### **Tree Deep Dives**
- [StatQuest Decision Trees](https://www.youtube.com/watch?v=7VeUAPZLtww) - Josh Starmer visual explanation
- [Random Forests Clearly Explained](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) - StatQuest tutorial
- [Gini Impurity Explained](https://www.youtube.com/watch?v=umtjlg9I8vs) - Information theory in ML

---

## �🔗 Navigation

**[← Part 2: Classification](../Part-2/Part-2-Classification.md)** | **[Go to Exercises →](./Part-3-Exercises.md)** | **[Chapter 3 →](../README.md)**
