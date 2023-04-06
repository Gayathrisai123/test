from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)

@app.route('/')
def home():
  #return render_template('home.html')
   return "Home"

