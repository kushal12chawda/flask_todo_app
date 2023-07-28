from .models import Task

def response_serializer(tasks:Task):
    response =[]
    for task in tasks:
        task_dict={
            "task_id":task.task_id,
            "task_name":task.task_name,
            "task_desc":task.task_desc,
            "task_status":task.task_status,
        }

        response.append(task_dict)
    return response    
    