from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(UserMixin):
    def __init__(self,id,username,email,password):
        self.id=id
        self.username=username
        self.email=email
        self.password=password

    
    @classmethod
    def check_password(cls,encripted_password,password):
        return check_password_hash(encripted_password,password)