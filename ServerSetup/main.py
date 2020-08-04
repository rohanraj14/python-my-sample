from flask import Flask
from flask import send_from_directory
import os.path
app = Flask('app')
app = Flask(__name__, static_folder='static')  

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/<path:filename>')
def listfilms(filename):
  return send_from_directory(app.static_folder, filename)

app.run(host='0.0.0.0', port=8080)