"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(base)
    __tablename__ = 'users'

    id = db.Column(db.integer, primary_key=True)
    first_name = db.Column