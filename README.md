# Python Overflow

A database-driven Flask web application for browsing, adding, and managing Python libraries and their components — built for the CS2300 course project.

---

## 🚀 Features

- View all Python libraries
- Add new libraries via web form
- View detailed information on:
  - Functions
  - Modules
  - Versions
  - Contributors
- Built with Flask + SQLite and Bootstrap for styling

---

## 📁 Project Structure

python-library-app/ ├── app.py # Flask application ├── init_db.py # Initializes SQLite database ├── project_setup.sql # Schema + sample data ├── requirements.txt # Python dependencies ├── templates/ # HTML templates (Jinja2) ├── static/ # Optional static assets (CSS/JS) └── venv/ # Virtual environment (ignored in Git)
---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:TSanf0rd/Python-Overflow.git
cd Python-Overflow

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

3. Install Requirements
pip install -r requirements.txt

4. Initialize the Database
python init_db.py

5. Run the App
python app.py
Visit http://localhost:5000 in your browser.

👥 Team Members

[Add your teammates here]

📚 Technologies Used
Python 3.12

Flask 3.1

SQLite

Bootstrap 5


