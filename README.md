# 🐍 PythonOverflow: A Database of Python Libraries and Functions

PythonOverflow is a Flask-based web application that allows users to search, browse, and explore Python libraries and their built-in functions. It uses a custom-designed relational database powered by SQLite.

---

## 🚀 Features

- Browse Python libraries by category, license, and tags
- View detailed information including functions, modules, dependencies, and contributors
- Search and filter by keyword
- SQL admin panel for direct queries (admin only)
- Related library suggestions based on tags

---

## 🛠 Project Setup

> Clone and run the app locally on any machine with Python 3.7+

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pythonoverflow.git
cd pythonoverflow
```
## 2. Set up virtual envronment 

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python run_init_sql.py
```

### 5. Run the Flask app

```bash
python app.py
```

## Collaboration GuideLines 
