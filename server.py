"""Discover Playlist Project Server"""

# Standard Python Libraries
import os

# Flask
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

# Models
from model import connect_to_db, db

# Other External Libraries
import spotipy
spotify = spotipy.Spotify()

# Setting up Flask app
app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.secret_key = os.environ['APP_SECRET']


# API key and secret
spotify_consumer_key = os.environ['SPOTIFY_CONSUMER_KEY']
spotify_consumer_secret = os.environ['SPOTIFY_CONSUMER_SECRET']


# App Routes

@app.route('/')
def index():
    """"""

    return render_template("index.html")


# Running App

if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()
