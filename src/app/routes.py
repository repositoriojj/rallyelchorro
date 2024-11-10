from flask import render_template, send_from_directory
from . import app
app.template_folder = '../templates'

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename, cache_timeout=0)
@app.route('/')
def index():
    return render_template('index.html', title='Rally 12h El Chorro')