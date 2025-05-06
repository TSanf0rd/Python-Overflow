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

## 🐳 Run with Docker (Must be in a Linux environment to run install.sh)

### Prerequisites:
- [Docker](https://www.docker.com/) installed and running on your machine

### Steps:

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/pythonoverflow.git
cd pythonoverflow
```

2. **Run the install script**:
```bash
./install.sh
```
> 💡 This will build the Docker image and start the app at [http://localhost:5000](http://localhost:5000)

---

## 🔐 Admin Access

Visit [http://localhost:5000/login](http://localhost:5000/login) to log in as an admin.

---

## 🗂 Project Structure

```
├── app.py                  # Main Flask application
├── templates/              # Jinja2 HTML templates
├── static/                 # Optional static files (CSS/JS)
├── init.sql                # SQL schema and sample data
├── install.sh              # Docker install and run script
├── requirements.txt        # Python package dependencies
├── Dockerfile              # Docker image definition
└── README.md               # This file
```

---


### ⚠️ Notes
- The app runs on port 5000 by default. Ensure that port is not already in use.
- Make sure Docker is installed and running.
