from flask import Flask
from ._version import __version__


app = Flask(__name__)


from .routes import *

