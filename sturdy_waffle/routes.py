from flask import render_template
from . import app, __version__


@app.route("/")
def login():
    return render_template("login.html", version=__version__)
