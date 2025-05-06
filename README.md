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

### 2. Build the Docker Image
```bash
docker build -t pythonoverflow .
```
> 💡 This will build the Docker image and start the app at [http://localhost:5000](http://localhost:5000)

### 3. Run the Container
```bash
docker run -d -p 5000:5000 pythonoverflow
```

### 4. Open in Browser
Visit: [http://localhost:5000](http://localhost:5000)

## ⚙️ install.sh (for Linux/Mac)
If you prefer a single-command setup:
```bash
./install.sh
```
---
This will:
- Build the Docker image
- Run the container
- Launch the app at `http://localhost:5000`

## 📁 Database Information

The application uses a SQLite database file named `library.db`.

- ✅ This file contains all data used by the application — libraries, modules, versions, tags, and more.
- 📦 It is bundled with the Docker image when you run `docker build`.
- 🔄 If you want to start from scratch in the future, you could modify the app to run `init.sql` to rebuild `library.db` — but by default, the database is **preloaded with content**.
- ⚠️ Do **not delete** or ignore `library.db` unless you intend to reinitialize the schema and populate it manually.

## 👤 Admin Login
To access the admin dashboard, log in via the [http://localhost:5000/login](http://localhost:5000/login) link.

Default credentials (can be customized in code):
```
username: admin
password: admin
```

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
