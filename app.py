from flask import Flask, render_template, request
from flask import redirect, url_for, flash, session
import sqlite3

from flask_login import (
    LoginManager, UserMixin, login_user, login_required,
    logout_user, current_user
)

def get_all_modules():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                modules.mod_id, 
                modules.mod_name, 
                modules.mod_description, 
                library.lib_name, 
                modules.lib_id
            FROM modules
            JOIN library ON modules.lib_id = library.lib_id
        """)
        return cursor.fetchall()



app = Flask(__name__)
app.secret_key = 'supersecretkey123'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

DB_PATH = "library.db"

# --- Home Route ---
@app.route('/')
def home():
    return render_template("home.html")

# --- Admin Dashboard ---
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template("admin_dashboard.html")

# --- Browse/Search Route ---
@app.route('/browse')
def browse():
    search = request.args.get('search', '')
    license_filter = request.args.get('license', '')
    tag_filter = request.args.get('tag', '')

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT license FROM library")
        licenses = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT tag_id, tag_name FROM tag")
        tags = cursor.fetchall()

        query = """
            SELECT DISTINCT library.lib_id, library.lib_name, library.category, library.license, library.author
            FROM library
            LEFT JOIN lib_tag ON library.lib_id = lib_tag.lib_id
            LEFT JOIN tag ON lib_tag.tag_id = tag.tag_id
            WHERE 1=1
        """
        params = []

        if search:
            query += " AND (library.lib_name LIKE ? OR library.category LIKE ?)"
            params += [f"%{search}%", f"%{search}%"]

        if license_filter:
            query += " AND library.license = ?"
            params.append(license_filter)

        if tag_filter:
            query += " AND tag.tag_id = ?"
            params.append(tag_filter)

        cursor.execute(query, params)
        results = cursor.fetchall()

    return render_template("browse.html", results=results, licenses=licenses, tags=tags)

# --- SQL Query Tool (Admin Access) ---
@app.route('/execute', methods=['GET', 'POST'])
@login_required
def execute():
    query = ""
    result = ""

    if request.method == 'POST':
        query = request.form['sql']
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                if query.lower().strip().startswith("select"):
                    columns = [description[0] for description in cursor.description]
                    rows = cursor.fetchall()
                    result = {"columns": columns, "rows": rows}
                else:
                    conn.commit()
                    result = "Query executed successfully"
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", query=query, result=result)

# --- Library Detail Page ---
@app.route('/library/<int:lib_id>')
def library_detail(lib_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT lib_name, category, lib_description, license, install_instructions, author, doc_url
            FROM library WHERE lib_id = ?
        """, (lib_id,))
        library = cursor.fetchone()

        cursor.execute("SELECT func_name, func_description FROM function WHERE lib_id = ?", (lib_id,))
        functions = cursor.fetchall()

        cursor.execute("SELECT mod_name, mod_description FROM modules WHERE lib_id = ?", (lib_id,))
        modules = cursor.fetchall()

        cursor.execute("SELECT version_id, release_date, change_log FROM version WHERE lib_id = ?", (lib_id,))
        versions = cursor.fetchall()

        cursor.execute("""
            SELECT version.version_id, contributors.con
            FROM contributors
            JOIN version ON contributors.ver_id = version.version_id
            WHERE version.lib_id = ?
        """, (lib_id,))
        contributors = cursor.fetchall()

        cursor.execute("""
            SELECT l2.lib_name 
            FROM dependency d
            JOIN library l2 ON d.depend_id = l2.lib_id
            WHERE d.lib_id = ?
        """, (lib_id,))
        dependencies = cursor.fetchall()

        cursor.execute("""
            SELECT tag.tag_id, tag.tag_name
            FROM tag
            JOIN lib_tag ON tag.tag_id = lib_tag.tag_id
            WHERE lib_tag.lib_id = ?
        """, (lib_id,))
        tags = cursor.fetchall()

        cursor.execute("""
            SELECT DISTINCT l.lib_id, l.lib_name
            FROM library l
            JOIN lib_tag lt ON l.lib_id = lt.lib_id
            WHERE lt.tag_id IN (
                SELECT tag_id FROM lib_tag WHERE lib_id = ?
            ) AND l.lib_id != ?
        """, (lib_id, lib_id))
        related = cursor.fetchall()

    return render_template("library_detail.html",
                           library=library,
                           functions=functions,
                           modules=modules,
                           versions=versions,
                           contributors=contributors,
                           dependencies=dependencies,
                           tags=tags,
                           related=related)

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "admin"
        self.password = "adminpass"

users = {"admin": User(id="admin")}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)

        if user and password == user.password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin/libraries')
@login_required
def manage_libraries():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT lib_id, lib_name, category, license FROM library")
        libraries = cursor.fetchall()
    return render_template("admin_libraries.html", libraries=libraries)

@app.route('/admin/library/add', methods=['GET', 'POST'])
@login_required
def add_library():
    if request.method == 'POST':
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Get the current max lib_id
            cursor.execute("SELECT MAX(lib_id) FROM library")
            max_id = cursor.fetchone()[0]
            new_lib_id = (max_id or 0) + 1

            data = (
                new_lib_id,
                request.form['category'],
                request.form['lib_name'],
                request.form['lib_description'],
                request.form['license'],
                request.form['install_instructions'],
                request.form['author'],
                request.form['doc_url']
            )

            cursor.execute("""
                INSERT INTO library (lib_id, category, lib_name, lib_description, license, install_instructions, author, doc_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, data)
            conn.commit()
        return redirect(url_for('manage_libraries'))
    return render_template("add_library.html")



@app.route('/admin/library/<int:lib_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_library(lib_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            data = (
                request.form['category'],
                request.form['lib_name'],
                request.form['lib_description'],
                request.form['license'],
                request.form['install_instructions'],
                request.form['author'],
                request.form['doc_url'],
                lib_id
            )
            cursor.execute("""
                UPDATE library SET category=?, lib_name=?, lib_description=?, license=?, install_instructions=?, author=?, doc_url=?
                WHERE lib_id=?
            """, data)
            conn.commit()
            return redirect(url_for('manage_libraries'))

        cursor.execute("SELECT * FROM library WHERE lib_id = ?", (lib_id,))
        library = cursor.fetchone()
    return render_template("edit_library.html", library=library)

@app.route('/admin/library/<int:lib_id>/delete', methods=['POST'])
@login_required
def delete_library(lib_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM library WHERE lib_id = ?", (lib_id,))
        conn.commit()
    return redirect(url_for('manage_libraries'))

@app.route('/admin/function/add/<int:lib_id>', methods=['GET', 'POST'])
@login_required
def add_function(lib_id):
    if request.method == 'POST':
        data = (
            request.form['func_name'],
            request.form['source_code'],
            request.form['func_description'],
            lib_id
        )
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO function (func_name, source_code, func_description, lib_id)
                VALUES (?, ?, ?, ?)
            """, data)
            conn.commit()
        return redirect(url_for('library_detail', lib_id=lib_id))
    return render_template("add_function.html", lib_id=lib_id)

@app.route('/admin/function/edit/<string:func_name>', methods=['GET', 'POST'])
@login_required
def edit_function(func_name):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            data = (
                request.form['source_code'],
                request.form['func_description'],
                func_name
            )
            cursor.execute("""
                UPDATE function SET source_code = ?, func_description = ?
                WHERE func_name = ?
            """, data)
            conn.commit()
            cursor.execute("SELECT lib_id FROM function WHERE func_name = ?", (func_name,))
            lib_id = cursor.fetchone()[0]
            return redirect(url_for('library_detail', lib_id=lib_id))

        cursor.execute("SELECT * FROM function WHERE func_name = ?", (func_name,))
        function = cursor.fetchone()
    return render_template("edit_function.html", function=function)

@app.route('/admin/function/delete/<string:func_name>', methods=['POST'])
@login_required
def delete_function(func_name):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT lib_id FROM function WHERE func_name = ?", (func_name,))
        lib_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM function WHERE func_name = ?", (func_name,))
        conn.commit()
    return redirect(url_for('library_detail', lib_id=lib_id))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    submitted = False
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
            conn.commit()

        submitted = True

    return render_template('feedback.html', submitted=submitted)

# --- Admin: Modules ---

@app.route('/admin/modules')
@login_required
def manage_modules():
    modules = get_all_modules()
    return render_template("manage_modules.html", modules=modules)

@app.route('/admin/module/add', methods=['GET', 'POST'])
@login_required
def add_module():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT lib_id, lib_name FROM library")
        libraries = cursor.fetchall()

        if request.method == 'POST':
            data = (
                request.form['mod_name'],
                request.form['mod_code'],
                request.form['mod_description'],
                request.form['lib_id']
            )
            cursor.execute("""
                INSERT INTO modules (mod_name, mod_code, mod_description, lib_id)
                VALUES (?, ?, ?, ?)
            """, data)
            conn.commit()
            return redirect(url_for('manage_modules'))

    return render_template("add_module.html", libraries=libraries)


@app.route('/admin/module/<int:mod_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_module(mod_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if request.method == 'POST':
            data = (
                request.form['mod_name'],
                request.form['mod_code'],
                request.form['mod_description'],
                mod_id
            )
            cursor.execute("""
                UPDATE modules
                SET mod_name = ?, mod_code = ?, mod_description = ?
                WHERE mod_id = ?
            """, data)
            conn.commit()
            cursor.execute("SELECT lib_id FROM modules WHERE mod_id = ?", (mod_id,))
            lib_id = cursor.fetchone()[0]
            return redirect(url_for('library_detail', lib_id=lib_id))

        cursor.execute("SELECT * FROM modules WHERE mod_id = ?", (mod_id,))
        module = cursor.fetchone()
    return render_template("edit_module.html", module=module)

@app.route('/admin/module/delete', methods=['POST'])
@login_required
def delete_module(mod_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT lib_id FROM modules WHERE mod_id = ?", (mod_id,))
        lib_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM modules WHERE mod_id = ?", (mod_id,))
        conn.commit()
    return redirect(url_for('library_detail', lib_id=lib_id))



# --- Run Flask Server ---
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
