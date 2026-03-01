# Chapter 3: Machine Learning Algorithms

**Week:** Week 3 | **Duration:** 5 Parts (35+ hours) | **Level:** Intermediate

---

## 🎯 Chapter Objective

Master fundamental ML algorithms by implementing them **from scratch** before using libraries.

By the end of this chapter, you will:
- ✅ Implement linear regression with gradient descent
- ✅ Build classification models (Logistic Regression)
- ✅ Construct decision trees and random forests
- ✅ Reduce dimensionality with PCA
- ✅ Train reinforcement learning agents with Q-Learning
- ✅ Understand when to use each algorithm

---

## 📋 Weekly Structure

| Part | Topic | Core Concepts | Capstone |
|------|-------|---------------|----------|
| **1** | Linear Regression | Gradient descent, MSE, Sigmoid function | GPA Predictor |
| **2** | Classification | Entropy, Gini Impurity, Decision Boundaries | Loan Approval System |
| **3** | Decision Trees & Random Forests | Information Gain, Tree Pruning, Ensemble Methods | Market Basket Analysis |
| **4** | Dimensionality Reduction (PCA) | Eigenvalues, Variance explained, Visualization | Data Compressor |
| **5** | Reinforcement Learning (Q-Learning) | Agents, Environments, Rewards, Q-Learning | Campus Navigation Simulation |

---

## 🏗️ Architecture Philosophy

**Progressive Complexity:** Build algorithms from first principles

- **Part 1:** Understand optimization (gradient descent) & linear prediction
- **Part 2:** Extend to classification (binary prediction with probabilities)
- **Part 3:** Tree-based learning (decision trees & ensembles)
- **Part 4:** Unsupervised learning (dimensionality reduction)
- **Part 5:** Decision-making under uncertainty (reinforcement learning)

**Key Principle:** Math → Code → Scikit-learn comparison

---

## 📂 Directory Structure

```
Chapter-3-ML-Algorithms/
├── README.md (this file)
├── Part-1/
│   ├── Part-1-Linear-Regression.md
│   └── Part-1-Exercises.md
├── Part-2/
│   ├── Part-2-Classification.md
│   └── Part-2-Exercises.md
├── Part-3/
│   ├── Part-3-Decision-Trees.md
│   └── Part-3-Exercises.md
├── Part-4/
│   ├── Part-4-Dimensionality-Reduction.md
│   └── Part-4-Exercises.md
└── Part-5/
    ├── Part-5-Reinforcement-Learning.md
    └── Part-5-Exercises.md
```

---

## 🎓 Learning Outcomes

### By Part 1 (Linear Regression)
- Understand cost functions (MSE)
- Implement gradient descent from scratch
- Build simple linear models
- Tune learning rate and iterations
- Create GPA predictor model

### By Part 2 (Classification)
- Implement logistic regression
- Calculate decision boundaries
- Understand entropy and Gini impurity
- Evaluate with precision/recall/F1
- Build loan approval classifier

### By Part 3 (Decision Trees & Random Forests)
- Build decision trees from scratch
- Understand information gain
- Implement tree pruning
- Build random forests (bagging)
- Analyze feature importance

### By Part 4 (Dimensionality Reduction - PCA)
- Implement PCA from scratch
- Calculate eigenvalues and eigenvectors
- Reduce high-dimensional data
- Visualize with scree plots
- Build data compressor

### By Part 5 (Reinforcement Learning - Q-Learning)
- Understand Markov Decision Processes (MDPs)
- Implement Q-Learning algorithm
- Build agents and environments
- Master exploration vs. exploitation
- Train navigation agent with rewards

---

## 🔧 Technologies and Libraries

### Core Math
```python
NumPy          # Matrix operations
Math           # Basic mathematics
```

### ML Libraries (for comparison)
```python
Scikit-learn   # Production models
```

### Visualization
```python
Matplotlib     # Plotting results
```

---

## 💡 Real-World Applications

1. **Housing Price Prediction** (Part 1)
   - Linear regression on house features
   - Predicting continuous values

2. **Customer Classification** (Part 2)
   - Binary/multiclass classification
   - Predicting customer categories

3. **Decision Trees for Classification** (Part 3)
   - Interpretable models
   - Feature importance analysis from tree splits

4. **High-Dimensional Data Compression** (Part 4)
   - Reducing dimensionality for visualization
   - Feature extraction from image/text data

5. **Autonomous Decision-Making** (Part 5)
   - Agent navigation and pathfinding
   - Robotics and game AI

---

## 📊 Assessment Criteria

### Part Exercises (40%)
- Correct algorithm implementation
- Code efficiency and clarity
- Proper error handling

### Part Capstones (60%)
- Working model on real data
- Proper evaluation metrics
- Comparison with scikit-learn

### Bonus (Extra Credit)
- Advanced optimization techniques
- Hyperparameter tuning
- Cross-validation implementation

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install numpy scikit-learn matplotlib pandas
```

### Workflow
1. Study the Part module content
2. Implement algorithm from scratch
3. Complete exercises
4. Build capstone project
5. Compare with scikit-learn implementation

---

## 📚 Core Concepts Map

```
PART 1: LINEAR REGRESSION
  Cost Function → Gradient Descent → Parameter Update
  
PART 2: CLASSIFICATION (Extends Part 1)
  Logistic Function → Cross-Entropy Loss → Decision Boundary
  
PART 3: DECISION TREES & RANDOM FORESTS
  Information Gain → Tree Construction → Ensemble Methods
  
PART 4: DIMENSIONALITY REDUCTION (PCA)
  Covariance Matrix → Eigendecomposition → PCA Projection
  
PART 5: REINFORCEMENT LEARNING (Q-Learning)
  Agents → Environments → Rewards → Bellman Equation → Q-Updates
```

---

## 🔗 Navigation

- **[← Back to Main](../README.md)**
- **[Part 1: Linear Regression →](./Part-1/)**

---

## 💬 Key ML Principles

1. **Learning Paradigms**
   - Parts 1-3: Supervised Learning (with labeled data)
   - Part 4: Unsupervised Learning (PCA for feature extraction)
   - Part 5: Reinforcement Learning (learn from interaction)

2. **Bias-Variance Tradeoff**
   - Complex models overfit
   - Simple models underfit
   - Find balance through validation

3. **Model Evaluation**
   - Train/test split essential
   - Use appropriate metrics per task
   - Cross-validation for robustness

4. **Feature Engineering**
   - Not all features equally important
   - Proper scaling and normalization needed
   - Feature selection and reduction crucial

5. **Algorithm Selection**
   - Linear data → linear models (Part 1)
   - Complex patterns → trees/forests (Part 3)
   - High dimensions → PCA (Part 4)
   - Decision-making → RL agents (Part 5)

---

## 📚 Learning Resources for Chapter 3

### **Linear Algebra Fundamentals**
- [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [NumPy Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [Wikipedia - Linear Algebra](https://en.wikipedia.org/wiki/Linear_algebra)

### **Optimization & Gradient Descent**
- [Gradient Descent Explained](https://en.wikipedia.org/wiki/Gradient_descent)
- [StatQuest - Gradient Descent Video](https://www.youtube.com/watch?v=sDv4f4s2SB8)
- [Optimizers Comparison](https://www.ruder.io/optimizing-gradient-descent/)
- [Backpropagation Algorithm](https://en.wikipedia.org/wiki/Backpropagation)

### **Classification & Decision Trees**
- [Decision Trees Explained](https://en.wikipedia.org/wiki/Decision_tree)
- [StatQuest - Decision Trees Playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUIE6oDioVv8sXvzc1QmKKpd)
- [Random Forests](https://en.wikipedia.org/wiki/Random_forest)
- [Information Gain & Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))

### **Dimensionality Reduction**
- [PCA (Principal Component Analysis)](https://en.wikipedia.org/wiki/Principal_component_analysis)
- [StatQuest - PCA Video](https://www.youtube.com/watch?v=_UVHneBUenI)
- [Eigenvalues and Eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

### **Reinforcement Learning**
- [Sutton & Barto - RL Book](http://incompleteideas.net/book/the-book-2nd.html)
- [OpenAI Spinning Up in Deep RL](https://spinningup.openai.com/)
- [Q-Learning Tutorial](https://www.youtube.com/watch?v=yMk_XwIlNjY)
- [Markov Decision Processes](https://en.wikipedia.org/wiki/Markov_decision_process)
- [Bellman Equation](https://en.wikipedia.org/wiki/Bellman_equation)

### **Scikit-learn & Practice**
- [Scikit-learn Official Guide](https://scikit-learn.org/stable/user_guide.html)
- [Hands-On Machine Learning Repository](https://github.com/ageron/handson-ml2)
- [Andrew Ng ML Course](https://www.coursera.org/learn/machine-learning)
- [Fast.ai Machine Learning](https://www.fast.ai/)

### **Evaluation & Metrics**
- [Scikit-learn Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
- [ROC Curve & AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
- [Cross Validation](https://scikit-learn.org/stable/modules/cross_validation.html)

---

## 📖 Chapter-Specific Resources

Each Part includes detailed "📚 Additional Resources" sections at the end with links to:
- Theory explanations
- Tutorial videos
- Research papers
- Implementation references
- Interactive visualizations

---

**Last Updated:** February 19, 2026 | **Status:** Complete with Resources
