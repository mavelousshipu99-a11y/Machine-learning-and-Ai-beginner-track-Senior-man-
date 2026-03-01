# Part 2: Git & GitHub - Version Control

**Duration:** 3-4 hours | **Level:** Beginner-Intermediate | **Prerequisites:** Part 1 (Python Environment)

---

## 📚 Overview

Git is a **version control system** that tracks changes to your code. GitHub is a **cloud platform** for sharing code. This Part covers:
- Installing Git
- Understanding commits and branches
- Using GitHub for backup and collaboration
- Workflow for this internship

---

## 🎯 Learning Outcomes

By the end of this Part, you will:
- ✅ Have Git installed and configured
- ✅ Understand commits, branches, and repositories
- ✅ Create a GitHub account and fork this course
- ✅ Push your work to GitHub
- ✅ Follow the commit strategy for this course

---

## 🔧 Part 1: Installing Git

### **Check if Git is Installed**

```bash
git --version
```

**Expected Output:**
```
git version 2.40.0  # or any version 2.0+
```

### **Install Git**

#### **Windows:**
1. Go to [git-scm.com](https://git-scm.com/)
2. Click "Download for Windows"
3. Run the installer
4. Accept default options (recommended)
5. Verify: Open Command Prompt and run `git --version`

#### **macOS:**
```bash
# Using Homebrew
brew install git

# Or download from git-scm.com
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

#### **Linux (Fedora):**
```bash
sudo dnf install git
```

---

## ⚙️ Part 2: Git Configuration

After installing, configure Git with your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Verify Configuration:**
```bash
git config --global --list
```

**Should show:**
```
user.name=Your Name
user.email=your.email@example.com
```

---

## 📖 Part 3: Git Basics

### **Key Concepts**

| Term | Meaning | Example |
|------|---------|---------|
| **Repository** | Folder tracked by Git | `seedai/` |
| **Commit** | Snapshot of code at a moment | "Part 1: Python setup" |
| **Branch** | Parallel version of code | `main`, `feature/nlp` |
| **Push** | Send commits to GitHub | `git push origin main` |
| **Pull** | Get commits from GitHub | `git pull origin main` |

### **Commit Workflow**

Every time you complete a Part, follow this pattern:

```bash
# 1. See what changed
git status

# 2. Stage all changes
git add .

# 3. Commit with descriptive message
git commit -m "Part-X: [Topic] completed - [Description]"

# 4. Push to GitHub
git push origin main
```

**Example Commit Messages:**
```bash
git commit -m "Part-1: Python Environment setup - created virtual environment"
git commit -m "Part-2: Text Preprocessing - implemented regex tokenizer"
git commit -m "Part-3: Linear Regression - built gradient descent from scratch"
```

### **Good Commit Messages**

✅ **Good:**
```
Part-1: Linear Regression - implemented gradient descent with batch updates
```

❌ **Bad:**
```
fix stuff
updated code
another change
```

**Formula for Good Messages:**
```
[Part-X]: [Topic] - [What you did]
```

---

## 🌐 Part 4: GitHub Setup

### **Step 1: Create GitHub Account**

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Enter email, password, username
4. Complete email verification
5. Set preferences (free plan is fine)

### **Step 2: Create SSH Key (Recommended)**

SSH makes pushing/pulling easier without passwords:

#### **Windows:**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter for all prompts (default location)
# Then run:
cat ~/.ssh/id_ed25519.pub
```

#### **macOS/Linux:**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter for all prompts
# Display public key:
cat ~/.ssh/id_ed25519.pub
```

### **Step 3: Add SSH Key to GitHub**

1. Copy the output from above (starts with `ssh-ed25519`)
2. Go to GitHub Settings → SSH and GPG keys
3. Click "New SSH key"
4. Paste your public key
5. Save

### **Step 4: Clone the Course Repository**

```bash
# Using SSH (if you set up SSH key above)
git clone git@github.com:yourusername/seedai.git
cd seedai

# Or using HTTPS (if you prefer)
git clone https://github.com/yourusername/seedai.git
cd seedai
```

---

## 📝 Part 5: Workflow for This Course

### **Daily Commit Strategy**

For **every Part you complete**, make a commit:

```bash
# After finishing Part 1 exercises
git add .
git commit -m "Part-1: Advanced Python - completed all exercises and capstone"
git push origin main

# After finishing Part 2 exercises
git add .
git commit -m "Part-2: Text Preprocessing - regex implementation and exercises done"
git push origin main
```

### **Example Week 1 Commits**

```
Part-1: Advanced Python - exercises completed
Part-2: Text Preprocessing - tokenizer built
Part-3: File Indexing - inverted index implemented
Part-4: Embeddings & Similarity - cosine similarity working
Part-5: NLP Integration - capstone Tiny NLP Engine completed
```

### **Branching Strategy (Optional)**

For more organization, use branches:

```bash
# Create a new branch for a Chapter
git checkout -b chapter/1-nlp

# Do your work...
git add .
git commit -m "Part-1: Advanced Python - completed"

# Merge back to main when done
git checkout main
git merge chapter/1-nlp
git push origin main
```

---

## 🚀 Part 6: Essential Git Commands

### **Check Status**
```bash
git status  # See what changed
```

### **View History**
```bash
git log --oneline  # See all commits
git log -5  # See last 5 commits
```

### **Make Changes**
```bash
git add .               # Stage all changes
git add filename.py     # Stage specific file
git commit -m "message" # Create commit
```

### **Update from GitHub**
```bash
git pull origin main  # Get latest changes from GitHub
```

### **Send to GitHub**
```bash
git push origin main  # Send your commits to GitHub
```

### **Undo Changes**
```bash
git restore filename.py        # Undo unstaged changes to a file
git restore --staged filename  # Unstage a file
git revert HEAD                # Undo last commit (creates new commit)
```

---

## 📊 Git Workflow Diagram

```
Your Computer              GitHub (Cloud)
     ↓                           ↓
  Working      git add      Staging      git commit      Local        git push       Remote
  Directory  --------→       Area     -----------→     Repository  -----------→   Repository
     ↑                           ↑                          ↑                           ↑
     └──────────────────────────git add .──────────────────┘                         │
                                                                                       │
                                        git pull ←────────────────────────────────────┘
```

---

## 🔗 Additional Resources

### **Git Documentation:**
- **Official Git Book:** [git-scm.com/book](https://git-scm.com/book/en/v2)
  - Complete reference for all Git concepts
  
- **Git Cheat Sheet:** [github.com/joshnh/Git-Commands](https://github.com/joshnh/Git-Commands)
  - Quick reference for common commands

### **Interactive Learning:**
- **Learn Git Branching:** [learngitbranching.js.org](https://learngitbranching.js.org/)
  - Interactive visual guide to Git branching
  
- **Git Immersion:** [gitimmersion.com](http://gitimmersion.com/)
  - Hands-on Git tutorial with examples

### **GitHub Documentation:**
- **GitHub Guides:** [guides.github.com](https://guides.github.com/)
  - Official GitHub tutorials
  
- **GitHub SSH Setup:** [docs.github.com/en/authentication/connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
  - Complete SSH key setup guide

### **Best Practices:**
- **Conventional Commits:** [conventionalcommits.org](https://www.conventionalcommits.org/)
  - Standard for writing commit messages
  
- **Why Every Software Developer Should Use Git:** [Medium Article](https://medium.com/hackernoon/why-every-software-developer-should-use-git-8fa891dba867)
  - Understand the importance of version control

### **Troubleshooting:**
- **Common Git Issues:** [oh-shit-git.com](https://oh-shit-git.com/)
  - Solutions to common Git mistakes
  
- **Stack Overflow Git Questions:** [stackoverflow.com/questions/tagged/git](https://stackoverflow.com/questions/tagged/git)
  - Community answers to Git problems

---

## ✅ Success Criteria

You've successfully completed Part 2 when:

- [ ] Git is installed (`git --version` works)
- [ ] Git is configured with your name and email
- [ ] GitHub account created
- [ ] SSH key set up (optional but recommended)
- [ ] Course repository cloned
- [ ] You can make and push commits to GitHub
- [ ] You understand the commit strategy for this course

---

## 🎓 Next Steps

Once you've completed this Part:
→ Move to **Part 3: Jupyter Notebooks & IDEs** to set up your development environment

---

**Part Status:** ✅ Complete  
**Difficulty:** ⭐⭐ (Beginner-Intermediate)  
**Time Estimate:** 3-4 hours  
**Key Takeaway:** Version control (Git) is essential for professional development and tracking your learning journey.
