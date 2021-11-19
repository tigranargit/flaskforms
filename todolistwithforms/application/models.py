from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(100))
    due = db.Column(db.DateTime)
    status = db.Column(db.String(50))