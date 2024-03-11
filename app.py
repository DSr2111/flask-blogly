"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
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

@app.route('/')
def root():
    """Homepage to list of users"""

    return redirect("/users")


@app.route('/users')
def users_index():
    """Show a page with information on all Blogly users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template(users/'index.html', users=users)


@app.route('/users/new', methods=["POST"])
def users_new():
    """Handles form submissions to create new users"""

    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)
    
    db.session.add(new_user)
    db.session.commit()

    """take client back to user list once new user is added"""
    return redirect("/users")

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def users_update(user_id):
    """Form handling to update user info"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()
    flash(f"User {user.full_name} updated")

    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.full_name} deleted.")

    return redirect("/users")

