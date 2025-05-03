from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Dummy user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "admin"
        self.password = "adminpass"  # Use env variable or hashing in production

# Only one user for now
users = {"admin": User(id="admin")}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)
