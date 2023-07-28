from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Todo, Task
from . import db
from flask_login import login_required,current_user,login_manager

views = Blueprint('views',__name__)

@views.route('/login_failed', methods =['GET','POST'])
def login_failed():
    return redirect(url_for('auth.login_get_user'))

@views.route('/signup_failed', methods =['GET','POST'])
def signup_failed():
    return redirect(url_for('auth.signup')) 

@views.route('/sign_up_success', methods =['GET','POST'])
def sign_up_success():
    return redirect(url_for('auth.login_get_user'))

@views.route('/home')
@login_required
def home():
    print("nice")
    print(current_user.user_id)
    todoall = Todo.query.filter(Todo.user_fk == current_user.user_id)
    if(Todo.user_fk == current_user.user_id):
        print("good")
    print(todoall)
    todoid = Todo.query.filter(Todo.user_fk == current_user.user_id).first()
    if (todoid == None):
        return render_template("new2.html", todo = todoall, todoid = todoid, user = current_user)
    print(todoid.todo_id)
    taskid = todoid.task
    print(current_user.user_id)
    return render_template("new.html", todo = todoall, task = taskid, todoid = todoid, user = current_user)    

# @views.route('/home')
# def home():
#     print("nice")
#     print(current_user.user_id)
#     todoall = Todo.query.filter(Todo.user_fk == current_user.user_id)
#     if(Todo.user_fk == current_user.user_id):
#         print("good")
#     print(todoall)
#     todoid = Todo.query.filter(Todo.user_fk == current_user.user_id).first()
#     print(todoid.todo_id)
#     taskid = todoid.task
#     print(current_user.user_id)
#     return render_template("new.html", todo = todoall, task = taskid, todoid = todoid, user = current_user)

@views.route('/todo_click/<int:id>', methods =['GET','POST'])
@login_required
def todo_click(id):
    todo = Todo.query.filter(Todo.user_fk == current_user.user_id)
    todoid = Todo.query.get(id)
    task = todoid.task
    return render_template("new.html",todo=todo,task=task, todoid = todoid, user = current_user)


@views.route('/add_task/<int:id>', methods=['GET', 'POST'])
@login_required
def add_task(id):
    if request.method == 'POST':
        n_task_name = request.form.get("taskname")
        n_task_desc = request.form.get("taskdesc")
        new_task = Task(task_name = n_task_name, task_desc = n_task_desc, task_status = False, user_fk = current_user.user_id, todo_fk = id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(request.referrer)
    
@views.route('/add_todo', methods=['GET', 'POST'])
@login_required
def add_todo():
    if request.method == 'POST':
        n_todo_name = request.form.get("todoname")
        print("meow")
        print(n_todo_name)
        new_todo = Todo(todo_name = n_todo_name, user_fk = current_user.user_id)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('views.home'))    
    
@views.route('/delete_task/<int:id>', methods=['GET', 'POST'])  
@login_required
def delete_task(id):
    task_to_delete = Task.query.get(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(request.referrer)

@views.route('/delete_todo/<int:id>', methods=['GET', 'POST']) 
@login_required 
def delete_todo(id):
    if request.method == "POST":
        todo_to_delete = Todo.query.get(id)
        db.session.delete(todo_to_delete)
        db.session.commit()
        return redirect(url_for('views.home'))

# @views.route('/update_task/<int:id>', methods=['GET', 'POST'])
# def update_task(id):
#     if request.method == "POST":
#         task_to_update = Task.query.get(id)
#         task_to_update.task_status = 1
#         db.session.commit()
#         return redirect(url_for('views.home'))

@views.route('/update_task/<int:id>', methods=['GET', 'POST'])
@login_required
def update_task(id):
    if request.method == "POST":
        task_to_update = Task.query.get(id)
        print(task_to_update.task_status)
        if task_to_update.task_status == True:
            task_to_update.task_status = False
        else:
            task_to_update.task_status = True 
        db.session.commit()
        return redirect(url_for('views.home'))        
    
# @views.route('/edit_name', methods=['GET', 'POST'])
# def edit_name():
#     if request.method == "POST":
#         todo_to_edit = Todo.query.get(2)
#         todo_to_edit.task_name = request.form.get("newname")
#         db.session.commit()
#         return redirect(url_for('views.home'))

@views.route('/edit_name/<int:id>/<string:y>', methods=['GET', 'POST'])
@login_required
def edit_name(id, y):
    if request.method == "POST":
        todo_to_edit = Todo.query.get(int(id))
        print(todo_to_edit)
        todo_to_edit.todo_name = y
        db.session.commit()
        return redirect(url_for('views.home'))