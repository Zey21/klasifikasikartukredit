from flask import Flask,render_template,request
import numpy as np
import pickle
import os
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def web():
    return render_template('index.html')

@app.route('/home',methods = ['POST','GET'])
def web1():
    return render_template('index.html')

@app.route('/fitur',methods = ['POST','GET'])
def web2():
    return render_template('sub.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
