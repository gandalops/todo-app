from flask import Blueprint, render_template, jsonify, request
from datetime import datetime
from bkend.services.task_service import add_task, get_all_tasks

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/version')
def version():
    return jsonify({"version": "fullstack-v6", "status": "running"})

@main_bp.route('/jenkins')
def jenkins_info():
    return jsonify({"pipeline": "Jenkins", "status": "success"})

@main_bp.route('/meta')
def meta():
    return jsonify({
        "version": "v6",
        "deployed": datetime.utcnow().isoformat() + "Z"
    })

@main_bp.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(get_all_tasks())

@main_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({"error": "Description is required"}), 400
    task = add_task(data['description'])
    return jsonify(task), 201

@main_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    from bkend.services.task_service import delete_task_by_id
    success = delete_task_by_id(task_id)
    if success:
        return jsonify({"message": "Task deleted"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

