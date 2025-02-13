from flask import Flask, render_template, request, redirect, flash, session
import sqlite3


app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/moments')
def mom():
    return render_template('moments.html')

@app.route('/gallery')
def gal():
    return render_template('gallery.html')



if __name__ == '__main__':
    app.run(debug=True)
