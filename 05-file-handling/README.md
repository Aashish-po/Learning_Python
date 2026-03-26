# File Handling

Reading from and writing to files.

## 📖 Topics Covered

- Opening and closing files
- Context managers (`with` statement)
- Reading files (`.read()`, `.readline()`, `.readlines()`)
- Writing files
- File modes (`r`, `w`, `a`, `r+`, etc.)
- Working with paths (`pathlib`)
- CSV files
- JSON files

---

## 🎯 Key Concepts

### Context Managers (Best Practice)
```python
# ❌ Old way (manual close)
f = open('file.txt', 'r')
content = f.read()
f.close()  # Might not run if error occurs!

# ✅ Modern way (automatic close)
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here
```

### Path Handling
```python
from pathlib import Path

# Modern path handling
base_dir = Path(__file__).parent
data_file = base_dir / 'data' / 'sales.csv'

# Check if exists
if data_file.exists():
    with open(data_file, 'r') as f:
        content = f.read()
```

### CSV Files
```python
import csv

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column_name'])

# Writing CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerow({'name': 'Aashish', 'age': 18})
```

---

## 🏋️ Exercises

### Exercise 1: Text File Processor
```python
# Read a text file
# Count words, lines, characters
# Find most common word
# Write statistics to new file
```

### Exercise 2: CSV Data Analysis
```python
# Read CSV file
# Filter rows by condition
# Calculate aggregates
# Write results to new CSV
```

### Exercise 3: JSON Configuration
```python
# Create config.json
# Read and parse
# Modify values
# Write back to file
```

---

## 🔗 Resources

- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [pathlib Guide](https://docs.python.org/3/library/pathlib.html)