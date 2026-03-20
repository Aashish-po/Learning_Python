# 🐍 Python Learning Journey

> A comprehensive guide to learning Python from basics to advanced topics, featuring hands-on exercises, real-world projects, and best practices.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Learning](https://img.shields.io/badge/Status-Active%20Learning-orange.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

---

## 📖 About This Repository

This repository documents my journey learning Python programming, from fundamental concepts to advanced topics like API integration, data analysis, and building real-world applications. Each section includes detailed notes, code examples, and practical exercises.

**Perfect for:**
- Beginners starting their Python journey
- Intermediate developers looking to solidify fundamentals
- Anyone interested in data science and API integration
- Students preparing for technical interviews

---

## 🎯 Learning Path

### ✅ Completed Topics

#### **Phase 1: Python Fundamentals**
- [x] Variables and Data Types
- [x] Operators and Expressions
- [x] Control Flow (if/else, loops)
- [x] Functions (definition, parameters, return values)
- [x] Scope (local vs global variables)
- [x] String Manipulation
- [x] Lists, Tuples, Dictionaries, Sets

#### **Phase 2: Modules & Packages**
- [x] Import Patterns
- [x] Built-in Modules (`datetime`, `os`, `json`, `random`)
- [x] Installing External Packages (`pip`)
- [x] Virtual Environments
- [x] requirements.txt Management

#### **Phase 3: External Tools & APIs**
- [x] Working with APIs (`requests` library)
- [x] JSON Data Handling
- [x] Error Handling for API Calls
- [x] API Authentication
- [x] HTTP Methods (GET, POST, PUT, DELETE)

#### **Phase 4: Data Analysis**
- [x] Pandas DataFrames
- [x] Data Processing and Cleaning
- [x] Statistical Analysis
- [x] Data Visualization (`matplotlib`)
- [x] Working with CSV Files

### 🚧 In Progress
- [ ] Object-Oriented Programming (OOP)
- [ ] File I/O Operations
- [ ] Regular Expressions
- [ ] Lambda Functions & Functional Programming

### 📋 Upcoming Topics
- [ ] Web Scraping (`BeautifulSoup`, `Selenium`)
- [ ] Database Integration (`SQLite`, `PostgreSQL`)
- [ ] Web Development (`Flask`, `FastAPI`)
- [ ] Testing (`pytest`, `unittest`)
- [ ] Asynchronous Programming
- [ ] Machine Learning Basics

---

## 📂 Repository Structure
```
python-learning/
├── 01-fundamentals/
│   ├── variables.py
│   ├── functions.py
│   ├── control_flow.py
│   └── exercises/
├── 02-modules-packages/
│   ├── imports.py
│   ├── virtual_env_guide.md
│   └── requirements.txt
├── 03-apis/
│   ├── weather_api.py
│   ├── github_api.py
│   └── api_examples/
├── 04-data-analysis/
│   ├── pandas_basics.py
│   ├── matplotlib_examples.py
│   ├── weather_analysis.py
│   └── data/
├── 05-projects/
│   ├── weather-dashboard/
│   ├── github-analyzer/
│   └── crypto-tracker/
├── exercises/
│   └── solutions/
├── notes/
│   └── best-practices.md
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package manager)
```

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/python-learning.git
cd python-learning
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run examples**
```bash
# Try the weather API example
python 03-apis/weather_api.py

# Analyze data
python 04-data-analysis/weather_analysis.py
```

---

## 🎓 Key Concepts & Examples

### Functions with Return Values
```python
def calculate_average(numbers):
    """Calculate average of a list of numbers."""
    return sum(numbers) / len(numbers)

scores = [85, 92, 78, 95, 88]
avg = calculate_average(scores)
print(f"Average: {avg}")  # Average: 87.6
```

### API Integration
```python
import requests

def get_weather(city, api_key):
    """Fetch current weather for a city."""
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    return {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
```

### Data Analysis with Pandas
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and analyze data
df = pd.read_csv('weather_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Create visualization
plt.plot(df['date'], df['temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trends')
plt.savefig('temperature_chart.png')
```

---

## 🛠️ Projects

### 1. Weather Dashboard
**Description:** Fetches 7-day weather data for multiple cities, analyzes trends, and generates visualizations.

**Technologies:** `requests`, `pandas`, `matplotlib`

**Features:**
- Historical weather data retrieval
- Multi-city comparison
- Temperature trend analysis
- Automated chart generation
- CSV export

[View Project →](05-projects/weather-dashboard/)

---

### 2. GitHub Repository Analyzer
**Description:** Analyzes GitHub user repositories and generates statistics.

**Technologies:** `requests`, `pandas`, `matplotlib`

**Features:**
- Repository statistics
- Language distribution
- Star/fork analysis
- Contribution timeline
- Visual dashboards

[View Project →](05-projects/github-analyzer/)

---

### 3. Cryptocurrency Price Tracker
**Description:** Tracks cryptocurrency prices and generates price trend reports.

**Technologies:** `requests`, `pandas`, `matplotlib`

**Features:**
- Real-time price fetching
- Historical data analysis
- Price change calculations
- Trend visualization
- Multi-coin comparison

[View Project →](05-projects/crypto-tracker/)

---

## 📚 Learning Resources

### Documentation
- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

### Libraries
- [Requests Documentation](https://requests.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

### Practice
- [LeetCode](https://leetcode.com/)
- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [Python Exercises](https://www.w3resource.com/python-exercises/)

### Communities
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [Python Discord](https://pythondiscord.com/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

---

## 💡 Best Practices I've Learned

### 1. Always Use Virtual Environments
```bash
# Create isolated environment for each project
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Error Handling for APIs
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
    return None
```

### 3. Secure API Keys
```python
# Use environment variables
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')  # Never hardcode!
```

### 4. Code Organization
```python
def main():
    """Main execution function."""
    # 1. Setup
    # 2. Process
    # 3. Save results

if __name__ == "__main__":
    main()
```

---

## 🤝 Contributing

While this is a personal learning repository, suggestions and improvements are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new example'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 Notes & Tips

### Common Pitfalls to Avoid
- ❌ Installing packages without activating virtual environment
- ❌ Using `from module import *` (causes naming conflicts)
- ❌ Hardcoding API keys in code
- ❌ Not handling API errors
- ❌ Forgetting to convert date strings to datetime objects

### Helpful Debugging Tips
- Use `print()` statements liberally
- Check data types with `type(variable)`
- Inspect DataFrames with `df.head()`, `df.info()`
- Use `try-except` blocks for error handling
- Read error messages carefully (start from bottom)

---

## 📊 Progress Tracking

| Topic | Status | Confidence | Practice Projects |
|-------|--------|------------|-------------------|
| Functions | ✅ Complete | ⭐⭐⭐⭐⭐ | 5+ |
| APIs | ✅ Complete | ⭐⭐⭐⭐ | 3 |
| Pandas | 🚧 Learning | ⭐⭐⭐ | 2 |
| OOP | 📋 Planned | - | 0 |
| Web Scraping | 📋 Planned | - | 0 |

---

## 🎯 Goals

### Short-term (1-2 months)
- [ ] Complete Object-Oriented Programming
- [ ] Build 5 complete projects
- [ ] Contribute to open-source Python project
- [ ] Master data analysis with pandas

### Long-term (3-6 months)
- [ ] Learn web development with Flask/FastAPI
- [ ] Explore machine learning basics
- [ ] Build full-stack web application
- [ ] Participate in coding competitions

---

## 📬 Connect

- **GitHub:** [@yourusername](https://github.com/yourusername)
- **LeetCode:** [@yourusername](https://leetcode.com/yourusername)
- **Email:** your.email@example.com

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Python community for excellent documentation
- Open-source contributors for amazing libraries
- Online tutorials and courses that helped me learn
- Everyone who provided feedback and suggestions

---

## 📅 Last Updated

March 20, 2026

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Happy Coding! 🚀**

</div>