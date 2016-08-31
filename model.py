"""Models and database functions for spotify discovery project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM


class User(db.Model):
    "User info."

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Event user_id=%s email =%s>" % (self.user_id,
                                                 self.email)


class Track(db.Model):
    "Track info."

    __tablename__ = "tracks"

    track_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spotify_track_id = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=True) #is this the best to use if I just want to save the date? Not the time

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Track track_id=%s date =%s>" % (self.track_id,
                                                 self.date)

class User_Track(db.Model):
    """Association table for tracks user has saved."""

    __tablename__ = "user_tracks"

    user_track_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('track.track_id'), nullable=False)


def connect_to_db(app, db_uri="postgresql:///noodledb"):
    """Connect the database to our Flask app."""

    # Configure to use postgres database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # If this module is run interactively, it will leave
    # you in a state of being able to work with the database directly.

    # To use Flask-SQLAlchemy, make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."