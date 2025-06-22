from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password_hash = db.Column('password_hash', db.String(128), nullable=False)
    
    @property
    def password(self):
        raise AttributeError("Password is write-only.")
    
    @password.setter
    def password(self, plaintext):
        self._password_hash = generate_password_hash(plaintext)
    
    def check_password(self, plaintext):
        return check_password_hash(self._password_hash, plaintext)
