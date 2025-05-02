from app import app, db
from app.models import Library

with app.app_context():
    lib = Library(
        name="Python Standard Library",
        author="Guido van Rossum",
        category="General",
        lib_description="The core set of built-in modules for Python.",
        doc_url="https://docs.python.org/3/library/"
    )

    db.session.add(lib)
    db.session.commit()
    print("Sample library added!")
