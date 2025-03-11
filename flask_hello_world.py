# Hello World Flask application
# python flask_hello_world.py

from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug = True)
else:
    pass