# Day 1: Data Acquisition & Exploration - Exercises

**Difficulty:** Foundational | **Time:** 6-7 hours | **Capstone:** The 'Dirty Data' Challenge

---

## 📝 Exercise Set 1: Loading and Exploring Data

### Exercise 1.1: Load CSV Data
Create a script that:
- Loads `data/customers.csv` using Pandas
- Prints shape, columns, and first 5 rows
- Displays data types of each column
- Shows summary statistics for numeric columns

**File:** `load_csv_data.py`
```python
# Your implementation here
```

**Expected Output:**
```
Shape: (1000, 5)
Columns: ['id', 'name', 'age', 'salary', 'department']
Data Types:
  id: int64
  name: object
  age: int64
  salary: float64
  department: object
```

---

### Exercise 1.2: Load JSON Data
Create a script that:
- Loads `data/products.json` using Pandas
- Handles nested JSON structures if present
- Explores the data structure
- Identifies data types

**File:** `load_json_data.py`

**Success Criteria:**
- [ ] JSON loaded without errors
- [ ] Nested structures handled properly
- [ ] Data types correctly identified
- [ ] Can print DataFrame summary

---

### Exercise 1.3: Explore with DataFrames
Create a script that:
- Loads any dataset
- Uses `.info()`, `.describe()`, `.dtypes`
- Displays unique value counts for categorical columns
- Shows memory usage of the dataset

**File:** `explore_dataframe.py`

**Bonus:** Create a reusable function `explore_dataset(df)` that automates all of this.

---

## 📝 Exercise Set 2: Handling Missing Values

### Exercise 2.1: Identify Missing Data
Create a script that:
- Loads a dataset with missing values
- Identifies all missing values
- Reports percentage missing per column
- Creates a missing data report DataFrame

**File:** `identify_missing.py`

**Expected DataFrame:**
```
         Column  Missing_Count  Missing_Percentage
0            id              0                 0.00
1          name              5                 0.50
2           age             15                 1.50
3        salary             20                 2.00
```

---

### Exercise 2.2: Handle Missing Values
Create a script that:
- Loads `data/messy_data.csv` (contains missing values)
- Implements 3 strategies:
  1. **Strategy 1:** Drop rows with any missing
  2. **Strategy 2:** Fill with mean/mode
  3. **Strategy 3:** Forward-fill (for time series)
- Saves each cleaned version to separate CSV files
- Reports rows before/after cleaning

**File:** `handle_missing_values.py`

**Success Criteria:**
- [ ] All 3 strategies implemented
- [ ] Outputs saved correctly
- [ ] Row counts reported
- [ ] No data loss explanation provided

---

### Exercise 2.3: Fill Missing Values Strategically
Create a function `smart_fill_missing(df)` that:
- Fills numeric columns with column mean
- Fills categorical columns with mode
- Fills date columns with forward-fill
- Reports what was filled

**File:** `smart_fill_missing.py`

---

## 📝 Exercise Set 3: Detecting & Removing Duplicates

### Exercise 3.1: Find Duplicates
Create a script that:
- Loads a dataset with duplicate rows
- Reports total duplicates
- Reports duplicates on specific columns (e.g., email)
- Shows which rows are duplicated

**File:** `find_duplicates.py`

**Output Example:**
```
Total duplicate rows: 15
Percentage: 1.5%
Duplicates by email: 8
```

---

### Exercise 3.2: Remove Duplicates
Create a script that:
- Loads `data/user_data.csv`
- Identifies and removes exact duplicates
- Removes duplicates keeping first occurrence
- Removes duplicates on key columns (email, phone)
- Saves cleaned data

**File:** `remove_duplicates.py`

**Success Criteria:**
- [ ] Exact duplicates removed
- [ ] Key-based deduplication works
- [ ] Different keep strategies tested
- [ ] Data saved correctly

---

### Exercise 3.3: Duplicate Analysis
Create a function that:
- Shows rows that are duplicated
- Identifies which columns have duplicate values
- Reports duplicate patterns
- Suggests which duplicates to keep

**File:** `analyze_duplicates.py`

---

## 📝 Exercise Set 4: Web Scraping with BeautifulSoup

### Exercise 4.1: Parse HTML
Create a script that:
- Fetches a sample HTML page (use requests library)
- Parses it with BeautifulSoup
- Extracts specific elements (titles, links, text)
- Prints structured output

**File:** `parse_html.py`

**Example Target:** Wikipedia, news site, product listing

```python
# Sample HTML to practice with
html = """
<div class="article">
    <h2 class="title">Article Title</h2>
    <p class="author">By John Doe</p>
    <p class="content">Article content here...</p>
    <a href="/link">Read more</a>
</div>
"""
```

---

### Exercise 4.2: Scrape Data into Lists
Create a script that:
- Scrapes product/article data from a website
- Extracts multiple attributes (title, price, rating)
- Stores in a list of dictionaries
- Converts to Pandas DataFrame

**File:** `scrape_to_dataframe.py`

**Success Criteria:**
- [ ] Data scraped successfully
- [ ] No errors in parsing
- [ ] DataFrame created
- [ ] Can be saved to CSV

---

### Exercise 4.3: Scrape with Error Handling
Create a robust scraper that:
- Handles missing elements gracefully
- Catches network errors
- Implements retry logic
- Logs errors and successes

**File:** `robust_scraper.py`

```python
def safe_scrape(url, selector):
    """Scrape with error handling"""
    try:
        response = requests.get(url, timeout=5)
        # Your code...
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
```

---

## 📝 Exercise Set 5: Exploratory Data Analysis (EDA)

### Exercise 5.1: Create Data Explorer Class
Create a `DataExplorer` class that:
- Takes a DataFrame in `__init__`
- Has method `summary()` - prints shape, dtypes, missing
- Has method `numeric_stats()` - prints mean, std, min, max
- Has method `categorical_stats()` - prints unique, most common
- Has method `full_report()` - prints comprehensive analysis

**File:** `data_explorer.py`

**Usage:**
```python
explorer = DataExplorer(df)
explorer.full_report()  # Print comprehensive report
```

---

### Exercise 5.2: Data Quality Score
Create a function `calculate_quality_score(df)` that:
- Returns score 0-100
- Penalizes for missing values
- Penalizes for duplicates
- Penalizes for extreme outliers
- Returns breakdown of penalties

**File:** `data_quality_score.py`

**Output:**
```
Data Quality Score: 85/100
- Missing values: -5 points
- Duplicates: -10 points
- Outliers: 0 points
```

---

### Exercise 5.3: Analysis Report Generator
Create a script that:
- Loads any dataset
- Generates comprehensive HTML report with:
  - Dataset overview (shape, types)
  - Missing data visualization-ready data
  - Duplicate analysis
  - Summary statistics
  - Column-by-column analysis
- Saves as HTML file

**File:** `report_generator.py`

---

## 🎯 Capstone: The 'Dirty Data' Challenge

### Project: CleanData - Dataset Cleaning System

**Scenario:**
You're given a messy real-world dataset with:
- Missing values (various percentages)
- Duplicate rows
- Inconsistent date formats
- Mixed data types
- Outliers and anomalies

**Deliverables:**

#### Part 1: Load & Explore (`part1_explore.py`)
```python
class DirtyDataCleaner:
    def __init__(self, filepath):
        # Load the messy dataset
        pass
    
    def generate_report(self):
        """Generate initial data quality report"""
        # Returns: {
        #   'total_rows': int,
        #   'total_columns': int,
        #   'missing_values': dict,
        #   'duplicates': int,
        #   'data_types': dict,
        #   'quality_score': float
        # }
        pass
```

#### Part 2: Clean (`part2_clean.py`)
Implement cleaning with these methods:
```python
class DirtyDataCleaner:
    def handle_missing_values(self):
        """Handle missing values strategically"""
        pass
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        pass
    
    def standardize_dates(self):
        """Convert all date columns to uniform format"""
        pass
    
    def fix_data_types(self):
        """Ensure correct data types"""
        pass
    
    def handle_outliers(self):
        """Identify and handle outliers"""
        pass
    
    def clean_all(self):
        """Run complete cleaning pipeline"""
        pass
```

#### Part 3: Validate (`part3_validate.py`)
```python
def validate_cleaned_data(original_df, cleaned_df):
    """Compare before/after"""
    report = {
        'rows_removed': len(original_df) - len(cleaned_df),
        'duplicates_removed': counting logic,
        'missing_values_fixed': ,
        'quality_improvement': new_score - old_score,
        'data_integrity': # All checks passed?
    }
    return report
```

#### Part 4: Generate Report (`part4_report.py`)
Output a summary:
```
DIRTY DATA CLEANING REPORT
==========================
Original dataset: 5000 rows, 15 columns
Cleaned dataset: 4850 rows, 15 columns

Actions taken:
- Removed 150 duplicate rows
- Fixed 245 missing values (various strategies)
- Standardized 3 date columns
- Corrected data types: 5 columns
- Handled 23 outliers

Quality Score: 65/100 → 92/100 (+27 points)

Cleaned data saved to: cleaned_data.csv
```

**Success Criteria:**
- [ ] Dataset loads without errors
- [ ] All missing values handled
- [ ] All duplicates removed
- [ ] Data types correct
- [ ] Quality score improved significantly
- [ ] Report generated
- [ ] Cleaned data saved

**Testing:**
```python
if __name__ == '__main__':
    cleaner = DirtyDataCleaner('data/dirty_data.csv')
    cleaner.generate_report()  # Initial report
    cleaner.clean_all()         # Run cleaning
    cleaner.generate_report()  # Final report
    cleaner.save('cleaned_data.csv')
```

---

## 📊 Datasets for Exercises

Suggested datasets to work with:
- **Customer Data:** Missing emails, duplicate IDs, inconsistent names
- **Sales Data:** Missing prices, mixed date formats, outlier values
- **User Data:** Duplicate accounts, missing ages, mixed encoding
- **Product Data:** Missing descriptions, duplicate SKUs, price inconsistencies

---

## 🔗 Navigation

**[← Back to Day 1 Module](./Day-1-Data-Acquisition.md)** | **[Chapter 2 →](../README.md)**
