from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '45cf93c4d41348cd9980674ade9a7356'

# Always put Routes at end
from todo_project import routes