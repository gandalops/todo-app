from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/version')
def version():
    return jsonify({"version": "fullstack-v5", "status": "running"})

@app.route('/jenkins')
def jenkins_info():
    return jsonify({"pipeline": "Jenkins", "status": "success"})

@app.route('/meta')
def meta():
    return jsonify({
        "version": "v5",
        "deployed": datetime.utcnow().isoformat() + "Z"
    })
