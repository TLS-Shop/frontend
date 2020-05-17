from flask_login import UserMixin
from datetime import datetime
from app import login
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin):
    id = None
    username = None
    email = None
    password_hash = None

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_passowrd(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_to_DB(self):
        return True


@login.user_loader()
def load_user(id):
