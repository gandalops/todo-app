from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <head>
                <title>DevOps Todo App</title>
                <style>
                    body { font-family: Arial; background-color: #f4f4f4; text-align: center; margin-top: 50px; }
                    h1 { color: #333; }
                    p { color: #555; }
                    .jenkins-msg {
                        color: blue;
                        font-weight: bold;
                        font-size: 2em;
                    }
                    .ci-badge {
                        background-color: #d3d3d3;
                        border: 1px solid #0000ff;
                        color: green;
                        padding: 10px;
                        margin: 20px auto;
                        width: 60%;
                        border-radius: 8px;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <h1>Hello Yogesh!</h1>
                <p>Welcome to the world of DevOps... </p>
                <p><strong>You're running <span style="color:#2a9df4;">Fullstack Version 4 🚀</span></strong></p>
                <p class="jenkins-msg">Automated by Jenkins CI 🚀</p>

                <div class="ci-badge">
                    ✅ CI/CD Verified & <code>/meta</code> route added in v4
                </div>
            </body>
        </html>
    '''

@app.route('/version')
def version():
    return jsonify({"version": "fullstack-v4", "status": "running"})

@app.route('/jenkins')
def jenkins_info():
    return jsonify({"pipeline": "Jenkins", "status": "success"})

@app.route('/meta')
def meta():
    return jsonify({
        "version": "v4",
        "deployed": datetime.utcnow().isoformat() + "Z"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
