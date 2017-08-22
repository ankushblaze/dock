#!flask/bin/python
from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('master.html')


@app.route('/mkdir', methods=['POST'])
def mkdir():
    directoryname = request.form['directoryname']
    data = {'directoryname': directoryname}
    headers = {'Content-Type': 'application/json'}
    content = requests.post("http://192.168.99.100:5001/",data=json.dumps(data),headers=headers)
    return content.text

@app.route('/cp', methods=['POST'])
def copy_files():
    source_file = request.form['file1']
    destination_file = request.form['file2']
    data = {'sourcefile': source_file,'destinationfile': destination_file}
    headers = {'Content-Type': 'application/json'}
    content = requests.post("http://192.168.99.100:5002/",data=json.dumps(data),headers=headers)
    return content.text

@app.route('/ls', methods=['GET'])
def list_files():
    content = requests.get("http://192.168.99.100:5003/")
    return render_template('listfiles.html',list_files = content.json()['files'])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')