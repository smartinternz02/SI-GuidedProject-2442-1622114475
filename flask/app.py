# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:50:31 2021

@author: Lasya Priya
"""

from flask import Flask,render_template,request
app =Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("index.html")
@app.route('/display',methods=['POST'])
def display():
    name=request.form['a']
    return render_template("index.html",y=name)
@app.route('/user/<name>')
def user(name):
    return "hello"+str(name)+"Welcome to the smart bridge user"
@app.route('/guest')
def guest():
    return "hey hello"
@app.route('/admin')
def admin():
    return "hii admin!"
if __name__=='__main__':
    app.run(debug=True)