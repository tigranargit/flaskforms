from application import app, db
from application.models import Tasks
from application.forms import AddTask, EditTask
from flask import render_template, request, redirect, url_for

from application.forms import AddTask, EditTask



@app.route('/tasks')

def view():
    tasks = Tasks.query.all()
    return render_template('viewtasks.html', tasks = tasks)


@app.route('/add', methods = ['GET', 'POST'])

def add():
    form = AddTask()
    if request.method == 'POST':
        name = form.task_name.data
        desc = form.task_desc.data
        due = form.due.data
        status = form.status.data
        if form.validate_on_submit:
            newtask = Tasks(name=name, desc=desc, due=due, status=status)
            db.session.add(newtask)
            db.session.commit()
        return redirect(url_for('view'))
    return render_template('addtask.html', form=form)


@app.route('/update/<int:id>', methods = ['GET', 'POST'])

def upd(id):
    form=EditTask()
    task = Tasks.query.get(id)
    if request.method == 'POST' and form.validate_on_submit():
        task.name = form.task_name.data
        task.desc = form.task_desc.data
        task.due = form.due.data
        task.status = form.status.data
        db.session.commit()
        return redirect(url_for('view'))
    return render_template('update.html', form=form, task=task)
   

@app.route('/delete/<int:id>')

def delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('view'))
