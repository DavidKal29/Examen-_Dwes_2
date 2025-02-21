from models.entities.user import User
from werkzeug.security import generate_password_hash

class ModelUser():
    
    @classmethod
    def login(cls,mongo,user):
        try:
            row=list(mongo.db.users.find({"email":user.email}))
            print('El row desde el login:',row)
            
            if row:
                id=row[0]["_id"]
                username=row[0]["username"]
                email=row[0]["email"]
                password=User.check_password(row[0]["password"],user.password)

                logged_user=User(id,username,email,password)

                return logged_user
            else:
                return None
            
        except Exception as err:
            print(err)
            return None
        


    @classmethod
    def register(cls,mongo,user):
        try:
            row=list(mongo.db.users.find({"email":user.email}))
            print('El row desde el register',row)

            if row:
                print('Usuario ya existe')
                return None
            else:
                mongo.db.users.insert_one({"username":user.username,"email":user.email,"password":generate_password_hash(user.password)})

                print('Usuario creado con exito crack')

                row=list(mongo.db.users.find({"email":user.email}))
            
                print(row)

                if row:
                    id=row[0]["_id"]
                    username=row[0]["username"]
                    email=row[0]["email"]
                    password=User.check_password(row[0]["password"],user.password)

                    logged_user=User(id,username,email,password)

                    return logged_user
                else:
                    return None

        except Exception as err:
            print(err)
            return None
        

    @classmethod
    def get_by_id(cls,mongo,id):
        try:
            row=list(mongo.db.users.find({"_id":id}))
            print('El row:',row)
            
            if row:
                id=row[0]["_id"]
                username=row[0]["username"]
                email=row[0]["email"]

                logged_user=User(id,username,email,None)

                return logged_user
            else:
                return None
            
        except Exception as err:
            print(err)
            return None
        
                
        