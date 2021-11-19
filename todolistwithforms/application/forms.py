from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms import validators 
from wtforms.validators import DataRequired

class AddTask(FlaskForm):
    task_name = StringField('Enter a task name', validators=[DataRequired()])
    task_desc = StringField('Enter task description', validators=[DataRequired()])
    due = DateField('Due date', format='%Y-%m-%d', validators=[DataRequired()])
    status = SelectField('Status', choices=[('todo','To-Do'), ('done', 'Done')], validators = [DataRequired()])
    submit = SubmitField('Add Task')

class EditTask(FlaskForm):
    task_name = StringField('Enter a task name', validators=[DataRequired()])
    task_desc = StringField('Enter task description', validators=[DataRequired()])
    due = DateField('Due date', format='%Y-%m-%d', validators=[DataRequired()])
    status = SelectField('Status', choices=[('todo','To-Do'), ('done', 'Done')], validators = [DataRequired()])
    submit = SubmitField('Update Task')
    