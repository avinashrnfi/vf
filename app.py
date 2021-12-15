#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:25:02 2021

@author: Avinash rnfi
@heroku test for deployment
"""
import numpy as np
from flask import Flask,request, jsonify, render_template


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8089,debug=True)