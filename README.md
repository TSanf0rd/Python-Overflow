# 🐍 PythonOverflow: A Database of Python Libraries and Functions

PythonOverflow is a Flask-based web application that allows users to search, browse, and explore Python libraries and their built-in functions. It uses a custom-designed relational database powered by SQLite.

---

## 🚀 Features

- Browse Python libraries by category, license, and tags
- View detailed information including functions, modules, dependencies, and contributors
- Search and filter by keyword
- SQL admin panel for adding/editing/removing libraries, modules, and more
- Related library suggestions based on tags
- Supports Docker for easy deployment

---

## 🐳 Run with Docker

### 1. Clone the repository

```bash
git clone https://github.com/TSanf0rd/python-overflow.git
cd pythonoverflow
```

### 2. Build the Docker image

```bash
docker build -t pythonoverflow .
```

### 3. Run the container

```bash
docker run -d -p 5000:5000 pythonoverflow
```

### 4. open your browser and go to:
```bash
http://localhost:5000
```

### ⚠️ Notes
- The app runs on port 5000 by default. Ensure that port is not already in use.
- Make sure Docker is installed and running.
