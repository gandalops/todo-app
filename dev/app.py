# dev/app.py

from flask import Flask
from bkend.routes.main import main_bp

app = Flask(__name__,
            template_folder='ftend/templates',
            static_folder='ftend/static')

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
