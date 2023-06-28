import todo_manager

task1 = {"title": "Task 1", "description": "Do something"}
task2 = {"title": "Task 2", "description": "Do something else"}

todo_manager.create_task(task1)
todo_manager.create_task(task2)

tasks = todo_manager.get_tasks()
for task in tasks:
    print(task)

task_id = 1  
new_task = {"title": "Updated Task", "description": "Updated description"}
todo_manager.update_task(task_id, new_task)

todo_manager.delete_task(task_id)