from app import app
from flask import render_template
from .forms import LoginForm


@app.route('/')
def index():

    user = {'username': 'Brian'}
    title = 'Microblog'

    posts = [
        {
            'author': {'username': 'Kamau'},
            'body': "Beautiful day to learn Flask! Don't you agree?"
        },

        {
            'author': {'username': 'Otieno'},
            'body': "Fast and Furious 9 gonna be lit!"
        },
        
    ]

    return render_template('index.html', title=title, user=user, posts = posts)


@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', title='Sign In', form=form )