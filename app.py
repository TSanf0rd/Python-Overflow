from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB_PATH = "library.db"

# --- Home Route ---
@app.route('/')
def home():
    return render_template("home.html")

# --- Browse/Search Route ---
@app.route('/browse')
def browse():
    search = request.args.get('search', '')
    license_filter = request.args.get('license', '')
    tag_filter = request.args.get('tag', '')

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Get distinct license and tag values
        cursor.execute("SELECT DISTINCT license FROM library")
        licenses = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT tag_id, tag_name FROM tag")
        tags = cursor.fetchall()

        # Build base query
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

        # Library core info
        cursor.execute("""
            SELECT lib_name, category, lib_description, license, install_instructions, author, doc_url
            FROM library WHERE lib_id = ?
        """, (lib_id,))
        library = cursor.fetchone()

        # Functions
        cursor.execute("SELECT func_name, func_description FROM function WHERE lib_id = ?", (lib_id,))
        functions = cursor.fetchall()

        # Modules
        cursor.execute("SELECT mod_name, mod_description FROM modules WHERE lib_id = ?", (lib_id,))
        modules = cursor.fetchall()

        # Versions
        cursor.execute("SELECT version_id, release_date, change_log FROM version WHERE lib_id = ?", (lib_id,))
        versions = cursor.fetchall()

        # Contributors by version
        cursor.execute("""
            SELECT version.version_id, contributors.con
            FROM contributors
            JOIN version ON contributors.ver_id = version.version_id
            WHERE version.lib_id = ?
        """, (lib_id,))
        contributors = cursor.fetchall()

        # Dependencies
        cursor.execute("""
            SELECT l2.lib_name 
            FROM dependency d
            JOIN library l2 ON d.depend_id = l2.lib_id
            WHERE d.lib_id = ?
        """, (lib_id,))
        dependencies = cursor.fetchall()

        # Tags for this library
        cursor.execute("""
            SELECT tag.tag_id, tag.tag_name
            FROM tag
            JOIN lib_tag ON tag.tag_id = lib_tag.tag_id
            WHERE lib_tag.lib_id = ?
        """, (lib_id,))
        tags = cursor.fetchall()

        # Related libraries with shared tags
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

# --- Run Flask Server ---
if __name__ == "__main__":
    app.run(debug=True)
