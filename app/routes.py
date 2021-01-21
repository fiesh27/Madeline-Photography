from app import app

import os

from flask import render_template, redirect, url_for

@app.route('/')
def intro():
    return render_template('index.html')