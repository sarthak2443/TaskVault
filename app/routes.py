from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .extensions import db

from .models import Task

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'msg': 'TaskVault API working!'})

# Create a new task
@main.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    user_id = get_jwt_identity()

    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        user_id=user_id
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'msg': 'Task created successfully'}), 201

# Get all tasks for current user
@main.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at
    } for task in tasks]), 200

# Update task
@main.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({'msg': 'Task not found'}), 404

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    db.session.commit()

    return jsonify({'msg': 'Task updated successfully'}), 200

# Delete task
@main.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({'msg': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'msg': 'Task deleted successfully'}), 200
