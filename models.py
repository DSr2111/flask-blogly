"""Models for Blogly."""
"""importing lib and setting up constants"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):
    """Setting up Blogly Users."""
    __tablename__ = 'users'

    id = db.Column(db.integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """ Getter that returns full name."""
        return f"{self.first_name} {self.last_name}"
    

class Post(db.model):
    """Posts"""
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now)
    user_id = db.column(db.Integer, db.ForeignKey('users.id'), nullable=False)

@property
def friendly_date(self):
    """Return a formatted date"""

    return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p") 


class Tag(db.Model):
    """Tag that can be added to posts."""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship(
        'Post',
        secondary="posts_tags",
        # cascade="all,delete",
        backref="tags",
    )

class PostTag(db.Model):
     """Tag on a post"""

     __tablename__ = "posts_tags"

     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
     tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)


def connect_db(app):
        """Connect to our Flask app."""

        db.app = app
        db.init_app(app)

