# APIs and Integration

Connecting Python to external services.

## 📖 Topics Covered

- HTTP requests with `requests` library
- REST API basics
- JSON parsing
- Authentication (API keys, tokens)
- Error handling for network requests
- Rate limiting

---

## 🎯 Key Concepts

### Making API Requests
```python
import requests

# GET request
response = requests.get('https://api.github.com/users/Aashish-po')
data = response.json()

# POST request
response = requests.post(
    'https://api.example.com/data',
    json={'key': 'value'},
    headers={'Authorization': 'Bearer token'}
)
```

### Error Handling
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise error for bad status
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## 🏋️ Exercises

### Exercise 1: Weather API Client
```python
# Create a weather client that:
# - Fetches current weather
# - Handles API errors
# - Caches results
```

### Exercise 2: GitHub API Wrapper
```python
# Create a GitHub client that:
# - Gets user info
# - Lists repositories
# - Handles rate limiting
```

---

## 🔗 Resources

- [requests Documentation](https://requests.readthedocs.io/)
- [REST API Tutorial](https://restfulapi.net/)