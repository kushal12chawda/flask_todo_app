from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
from . import db
from .models import User,Todo,Task
from .serializer  import response_serializer

api = Api()

parser = reqparse.RequestParser()
parser.add_argument('task_name')
parser.add_argument('task_desc')
parser.add_argument('task_status')

class TaskList(Resource):
    def get(self):
        tasks = Task.query.all()
        response = response_serializer(tasks)
        return response,200

    def post(self):
        data = parser.parse_args()
        data['task_name'] = str(data["task_name"])
        data['task_desc'] = str(data["task_desc"])
        data['task_status'] = bool(data["task_status"])
        new_data = Task(**data)
        db.session.add(new_data)
        db.session.commit()
        return data,201   
        
class TaskId(Resource):
    def get(self,id):
        task = Task.query.get(int(id))      

        if task:
            response = response_serializer([task])
            return response,200

        else:
            return {"mssg":"Not found"},404 

    def put(self,id):
        data = parser.parse_args()
        data['task_name'] = str(data["task_name"])
        data['task_desc'] = str(data["task_desc"])
        print(data['task_desc'])
        data['task_status'] = bool(data["task_status"])

        task = Task.query.get(int(id))

        if task:
            task.task_name = data.get("task_name")
            task.task_desc = data.get("task_desc")
            task.status = data.get("task_status")

            db.session.commit()
            response = response_serializer([task])
            return response,200
        else:
            return {"mssg":"Not found"}

    def delete(self,id):
        task = Task.query.get(int(id))

        if task:
            db.session.delete(task)
            db.session.commit()
            return {"msg":"deleted"},200
        else:
            return {"msg":"Not found"},404    



api.add_resource(TaskList ,'/task')
api.add_resource(TaskId ,'/task/<int:id>')   



