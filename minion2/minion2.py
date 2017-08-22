#!flask/bin/python
from flask import Flask, request
from shutil import copyfile
import os

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    os.chdir(os.pardir+"/code/common_folder/")
    copyfile(request.get_json()['sourcefile'], request.get_json()['destinationfile'])
    return "Copied Successfully!!!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)