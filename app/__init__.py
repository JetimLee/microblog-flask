from flask import Flask

app = Flask(__name__)

#imported on bottom in order to avoid circular imports
from app import routes