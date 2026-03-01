# ✅ Student Setup Checklist

Before starting the internship, ensure you have everything set up and working. This checklist guides you through all required installations and verifications.

---

## 📋 Pre-Course Checklist (Complete Before Day 1)

### System & Environment Setup

- [ ] **Operating System:** Windows, macOS, or Linux with at least 4GB RAM
- [ ] **Python 3.8 or higher installed** - Verify: `python --version`
- [ ] **pip is installed** - Verify: `pip --version`
- [ ] **Git is installed** - Verify: `git --version`
- [ ] **Text Editor/IDE:** VS Code installed from [code.visualstudio.com](https://code.visualstudio.com/)

### Python Setup (Follow Chapter 0, Part 1)

- [ ] **Created a virtual environment**
  ```bash
  python -m venv seedai_env
  source seedai_env/bin/activate  # Linux/Mac
  seedai_env\Scripts\activate     # Windows
  ```
  
- [ ] **Verified virtual environment is activated** - Let's start with `(seedai_env)`
- [ ] **Upgraded pip**
  ```bash
  pip install --upgrade pip
  ```

### Required Libraries (Chapter 0, Part 4)

- [ ] **NumPy:** `pip install numpy` ✓ Verify: `python -c "import numpy; print(numpy.__version__)"`
- [ ] **Pandas:** `pip install pandas` ✓ Verify: `python -c "import pandas; print(pandas.__version__)"`
- [ ] **Scikit-learn:** `pip install scikit-learn` ✓ Verify: `python -c "import sklearn; print(sklearn.__version__)"`
- [ ] **Matplotlib:** `pip install matplotlib` ✓ Verify: `python -c "import matplotlib; print(matplotlib.__version__)"`
- [ ] **Jupyter:** `pip install jupyter` ✓ Verify: `jupyter --version`

### Optional but Recommended

- [ ] **Seaborn:** `pip install seaborn` - Advanced visualization
- [ ] **Requests:** `pip install requests` - Web scraping & APIs
- [ ] **BeautifulSoup4:** `pip install beautifulsoup4` - HTML parsing
- [ ] **NLTK:** `pip install nltk` - NLP tasks
- [ ] **Streamlit:** `pip install streamlit` - Web application framework
- [ ] **spaCy:** `pip install spacy` - Industrial NLP

### Git & GitHub Setup (Chapter 0, Part 2)

- [ ] **Git configured with your name**
  ```bash
  git config --global user.name "Your Full Name"
  ```
  
- [ ] **Git configured with your email**
  ```bash
  git config --global user.email "your.email@example.com"
  ```
  
- [ ] **GitHub account created** at [github.com](https://github.com)
- [ ] **SSH key generated** (Optional but recommended)
  ```bash
  ssh-keygen -t ed25519 -C "your.email@example.com"
  ```
  
- [ ] **SSH key added to GitHub** - See [GitHub SSH Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [ ] **Repository cloned locally**
  ```bash
  git clone <repository-url>
  ```

### IDE Setup (Chapter 0, Part 3)

#### VS Code Configuration
- [ ] **Python extension installed** - ID: `ms-python.python`
- [ ] **Pylance extension installed** - ID: `ms-python.vscode-pylance`
- [ ] **Jupyter extension installed** - ID: `ms-toolsai.jupyter`
- [ ] **Python interpreter selected** - Use your virtual environment
  ```
  Ctrl+Shift+P → Python: Select Interpreter → Choose seedai_env
  ```

#### Jupyter Notebook Setup
- [ ] **Test Jupyter launch:**
  ```bash
  jupyter notebook
  ```
  Browser opens with Jupyter interface
  
- [ ] **Can create new Python 3 notebook**
- [ ] **Can execute code cells successfully**

### Development Environment Verification

Run the Chapter 0 Part 1 verification script:

```bash
cd 1-Month-ML-Internship/Chapter-0-Platforms-Tools/Part-1
python test_setup.py
```

Expected output: **All 4 tests PASS**
```
test_python_version: PASS
test_required_libraries: PASS
test_optional_libraries: PASS
test_jupyter: PASS
```

---

## 📚 Chapter-by-Chapter Checklist

### Chapter 0: Platforms & Tools (Week 0)

**Module 1: Python Environment**
- [ ] Read: Part-1-Python-Environment.md
- [ ] Complete: All code examples
- [ ] Verify: Run test_setup.py successfully

**Module 2: Git & GitHub**
- [ ] Read: Part-2-Git-GitHub.md
- [ ] Setup: Git configuration
- [ ] Create: First test commit
- [ ] Practice: Git basic workflow

**Module 3: Jupyter & IDEs**
- [ ] Read: Part-3-Jupyter-IDEs.md
- [ ] Launch: First Jupyter notebook
- [ ] Create: Simple "Hello World" notebook
- [ ] Learn: Keyboard shortcuts (at least 5)

**Module 4: ML Libraries**
- [ ] Read: Part-4-ML-Libraries.md
- [ ] Code: Work through all library examples
- [ ] Verify: Can import and use each library

**Module 5: Data & Resources**
- [ ] Read: Part-5-Data-Resources.md
- [ ] Explore: Visit 3 recommended dataset sources
- [ ] Join: At least 1 community (Stack Overflow, Reddit, Kaggle)
- [ ] Bookmark: Resources for quick reference

### Chapter 1: Python & NLP Architecture (Week 1-2)

**Day 1: Advanced Python**
- [ ] Read: Day-1-Advanced-Python.md
- [ ] Complete: Day-1-Exercises.md (all exercises)
- [ ] Practice: 10+ LeetCode problems (Easy/Medium)
- [ ] Review: Additional resources section

**Day 2: Text Preprocessing**
- [ ] Read: Day-2-Text-Preprocessing.md
- [ ] Complete: Day-2-Exercises.md
- [ ] Code: Implement 3 tokenization methods
- [ ] Practice: Regular expressions (regex101.com)

**Day 3: File Indexing**
- [ ] Read: Day-3-File-Indexing.md
- [ ] Complete: Day-3-Exercises.md
- [ ] Build: Simple file indexer
- [ ] Test: Index various file types

**Day 4: Embeddings & Similarity**
- [ ] Read: Day-4-Embeddings-Similarity.md
- [ ] Complete: Day-4-Exercises.md
- [ ] Code: Implement cosine similarity
- [ ] Learn: Word2Vec concepts

**Day 5: NLP Integration**
- [ ] Read: Day-5-NLP-Integration.md
- [ ] Complete: Day-5-Exercises.md
- [ ] Build: Complete NLP pipeline
- [ ] Project: Text processing system

### Chapter 2: Data-Intensive Search (Week 3-4)

**Day 1: Data Acquisition**
- [ ] Read: Day-1-Data-Acquisition.md
- [ ] Complete: Day-1-Exercises.md
- [ ] Download: Data from Kaggle, UCI, Google
- [ ] Code: Load data from multiple formats

**Day 2: Feature Engineering**
- [ ] Read: Day-2-Feature-Engineering.md
- [ ] Complete: Day-2-Exercises.md
- [ ] Code: Implement scaling & normalization
- [ ] Practice: Create derived features

**Day 3: Data Visualization**
- [ ] Read: Day-3-Data-Visualization.md
- [ ] Complete: Day-3-Exercises.md
- [ ] Create: 5+ different plot types
- [ ] Visualize: Real datasets

**Day 4: Information Retrieval**
- [ ] Read: Day-4-Information-Retrieval.md
- [ ] Complete: Day-4-Exercises.md
- [ ] Code: Implement inverted index
- [ ] Build: Search engine prototype

**Day 5: Streamlit Search**
- [ ] Read: Day-5-Streamlit-Search.md
- [ ] Complete: Day-5-Exercises.md
- [ ] Deploy: Interactive search app
- [ ] Share: App with others

### Chapter 3: ML Algorithms (Week 5-6)

**Part 1: Linear Regression**
- [ ] Read: Part-1-Linear-Regression.md
- [ ] Complete: Part-1-Exercises.md
- [ ] Code: Implement linear regression
- [ ] Visualize: Cost function & gradients

**Part 2: Classification**
- [ ] Read: Part-2-Classification.md
- [ ] Complete: Part-2-Exercises.md
- [ ] Code: Logistic regression, SVM
- [ ] Train: A real classification model

**Part 3: Decision Trees**
- [ ] Read: Part-3-Decision-Trees.md
- [ ] Complete: Part-3-Exercises.md
- [ ] Code: Decision tree from scratch
- [ ] Visualize: Tree structure

**Part 4: Dimensionality Reduction**
- [ ] Read: Part-4-Dimensionality-Reduction.md
- [ ] Complete: Part-4-Exercises.md
- [ ] Code: Implement PCA
- [ ] Visualize: High-dimensional data

**Part 5: Reinforcement Learning**
- [ ] Read: Part-5-Reinforcement-Learning.md
- [ ] Complete: Part-5-Exercises.md
- [ ] Code: Q-Learning algorithm
- [ ] Simulate: MDP environment

---

## 🚀 Daily Routine Checklist

**Each Study Day:**

- [ ] **Morning (30 min):** Review yesterday's concepts
- [ ] **Core Learning (2-3 hours):** Read chapter material
- [ ] **Hands-On Coding (2 hours):** Complete exercises
- [ ] **Review & Reflect (30 min):** Summarize learnings
- [ ] **Git Commit:** Save work - `git commit -m "feat: Complete Day-X"`
- [ ] **Community Activity (15 min):** Q&A or documentation

**Weekly Review:**

- [ ] Sunday: Review entire week's material
- [ ] Create summary document
- [ ] Attempt additional challenges
- [ ] GitHub commit with weekly summary
- [ ] Plan next week's goals

---

## 🎯 Success Metrics

Track your progress with these metrics:

| Metric | Target | How to Track |
|--------|--------|--------------|
| **Git Commits** | 1+ per day | `git log --oneline` |
| **Exercises Completed** | 100% | Check all `*-Exercises.md` |
| **Code Quality** | Clean code | Share in code review |
| **Community Engagement** | 2+ posts/week | Stack Overflow, Reddit |
| **Projects Built** | 1 per chapter | Portfolio on GitHub |
| **Learning Resources Used** | 3+ per week | Browse LEARNING_RESOURCES.md |

---

## 🆘 Troubleshooting Quick Links

| Problem | Solution |
|---------|----------|
| Python not found after install | [Chapter 0 Part 1](./1-Month-ML-Internship/Chapter-0-Platforms-Tools/Part-1-Python-Environment.md#troubleshooting) |
| Git commands not working | [Chapter 0 Part 2](./1-Month-ML-Internship/Chapter-0-Platforms-Tools/Part-2-Git-GitHub.md#troubleshooting) |
| Jupyter notebook won't launch | [Chapter 0 Part 3](./1-Month-ML-Internship/Chapter-0-Platforms-Tools/Part-3-Jupyter-IDEs.md#troubleshooting) |
| Library import errors | [Chapter 0 Part 4](./1-Month-ML-Internship/Chapter-0-Platforms-Tools/Part-4-ML-Libraries.md#troubleshooting) |
| Need help with concepts | [LEARNING_RESOURCES.md](./LEARNING_RESOURCES.md) |

---

## 📞 Getting Help

1. **Check the troubleshooting sections** in each chapter
2. **Search existing resources** in LEARNING_RESOURCES.md
3. **Ask on Stack Overflow** with [python], [machine-learning] tags
4. **Join communities:** Kaggle, Reddit r/learnmachinelearning
5. **Review similar projects** on GitHub

---

## 🎓 Certificate of Completion

Once you've completed **50% of checkboxes above**, you've established strong fundamentals!

When you complete **90%**, you're ready for advanced ML topics.

When you complete **100%**, congratulations! You've completed the 1-Month ML Internship! 🎉

---

**Last Updated:** February 19, 2026  
**Version:** 1.0
