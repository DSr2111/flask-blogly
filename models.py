"""Models for Blogly."""
"""importing lib and setting up constants"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):
    """Setting up Blogly Users"""
    __tablename__ = 'users'

    id = db.Column(db.integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """ Getter that returns full name"""
        return f"{self.first_name} {self.last_name}"