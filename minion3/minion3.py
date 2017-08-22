#!flask/bin/python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
	path = os.pardir+"/code/common_folder"
	files = os.listdir(path)
	return jsonify(files=files)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)