#!flask/bin/python
from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    #print(request.args)
    #print(request.get_json())
    parent = os.pardir+"/code/common_folder"
    path = parent + "/" + request.get_json()['directoryname']
    os.mkdir(path);
    return "Successfully Created"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)