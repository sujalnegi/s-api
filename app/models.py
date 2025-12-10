from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(256))
    display_name = db.Column(db.String(256))
    sessions = db.relationship('UserSession', backref='user', lazy=True)

class UserSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(256))
    