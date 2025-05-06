# dev/app.py

from flask import Flask
from bkend.routes.main import main_bp
from bkend.services.task_service import init_db  # ⬅️ Import init_db

init_db()  # ⬅️ Ensure DB and tasks table are ready

app = Flask(__name__, template_folder='ftend/templates', static_folder='ftend/static') # ✅ Flask use default /templates and /static
            

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) #flask default port=5000
