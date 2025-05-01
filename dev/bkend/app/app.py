from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Yogesh! Welcome to the world of DevOps.\n\nCongratulations on your local deployment!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

