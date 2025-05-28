# Flask Server
# python server.py

from flask import Flask, jsonify

app = Flask(__name__)

# http://127.0.0.1:5000

@app.route('/hello')
def hello():
    return jsonify(message="Hello World! from the server")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
else:
    pass