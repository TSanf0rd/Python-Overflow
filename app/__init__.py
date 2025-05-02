from flask_appbuilder import AppBuilder, SQLA
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

from . import models

# Delay importing views to avoid circular import issue
def register_views():
    from . import views
register_views()

