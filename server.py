
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db
from jinja2 import StrictUndefined


app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """"""

    return render_template("index.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    # app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()

    import doctest
    doctest.testmod()