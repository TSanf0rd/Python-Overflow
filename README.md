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
password: adminpass
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

---

## 📘 User Manual

### Homepage
![image](https://github.com/user-attachments/assets/df012284-6d2f-43f6-a602-64ae24222e6c)

- Navigate to [http://localhost:5000](http://localhost:5000)
- Click **Browse Libraries** to explore existing libraries.

### Browsing Libraries
![image](https://github.com/user-attachments/assets/fa7a6220-b553-4f79-870d-c62173cc37b3)

- View details, modules, and functions associated with each library.
- Use the search/filter functions (if enabled).

### Admin Dashboard
![image](https://github.com/user-attachments/assets/982eef3d-9c01-4fe8-9bf6-ad4622df9904)

- Log in via `/login` as an admin.
- Access:
  - 📚 Manage Libraries
  - 🧩 Manage Modules
  - 🛠 SQL Query Tool
  - 🔍 Browse as User

![image](https://github.com/user-attachments/assets/71eb11e0-97c3-4c18-a482-21432791f54c)

### Adding a Library
1. Navigate to **Admin Dashboard > Add Library**
2. Fill in:
   - Category
   - Name
   - Description
   - License
   - Install instructions
   - Author
   - Documentation URL
3. Submit to save it to the database.

### Adding a Module
<img src="![Screenshot 2025-05-06 155324](https://github.com/user-attachments/assets/08b1b360-e0e6-4f38-a479-0623b5be5574)
" alt="Admin Dashboard" width="600" height="400"/>

![image](https://github.com/user-attachments/assets/439b08f4-82c3-4fd2-92d0-8a3a6c040fb5)

1. Go to **Manage Modules** or a specific Library detail page.
2. Click **Add Module**.
3. Enter:
   - Name, code (optional), and description
   - Select a library from the dropdown list
4. Submit to add.

### SQL Admin Tool
![image](https://github.com/user-attachments/assets/ad8ad01e-615c-4878-9102-c9df055861aa)

- Visit `/execute`
- Type any valid SQL query (e.g., `SELECT * FROM library;`)
- View output in table format

### Feedback Page
![image](https://github.com/user-attachments/assets/a5cfacde-21ef-49c4-8350-5dc779263b4d)
- Users can submit general feedback or suggestions via `/feedback`

---

## 🔒 Security
![image](https://github.com/user-attachments/assets/f73e1ab8-e921-42a0-8da4-b7d6c896162b)

- Admin-only pages are protected using Flask-Login
- SQL injection is mitigated using parameterized queries

---

## 🤝 Contributions
Feel free to fork the project, make improvements, and submit pull requests!

---

## 📄 License
This project is licensed under PythonOverflow



