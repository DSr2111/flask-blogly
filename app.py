"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolBarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'iwlas4eae'

toolbar = DebugToolBarExtension(app)

connect_db(app)
db.create_all()

@app.route('/users')
def users_index():
    """Show a page with information on all Blogly users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template(users/'index.html', users=users)