from flask import Flask
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
                </style>
            </head>
            <body>
                <h1>Hello Yogesh!</h1>
                <p>Welcome to the world of DevOps... </p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


