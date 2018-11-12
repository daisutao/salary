from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

from salary.models import User

debug_toolbar = DebugToolbarExtension()

login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
