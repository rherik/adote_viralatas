from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/history")
@login_required
def historia():
    return render_template("historia.html", user=current_user)

@views.route("/signup", methods=['GET', 'POST'])
def sign():
    return render_template("signup.html", user=current_user)

@views.route("/login")
def login():
    return render_template("login.html", user=current_user)


@views.route("/crie", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        if not text:
            flash('Post não pode estar vazio', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Postagem criada!', category='success')
    return render_template('create_post.html', user=current_user)