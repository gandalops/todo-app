# bkend/services/task_service.py

tasks = []

def add_task(description):
    task = {"id": len(tasks) + 1, "description": description}
    tasks.append(task)
    return task

def get_all_tasks():
    return tasks

def delete_task_by_id(task_id):
    global tasks
    initial_count = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    return len(tasks) < initial_count
