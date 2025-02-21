from flask import Flask,request,render_template,jsonify,flash
from flask_login import current_user,login_user,logout_user,login_manager
from flask_pymongo import PyMongo
from models.entities.user import User
from models.modeluser import ModelUser
from werkzeug.security import generate_password_hash

app=Flask(__name__)
app.config['MONGO_URI']="mongodb+srv://david:david@prueba.7tbag.mongodb.net/flaskexamendwes?retryWrites=true&w=majority&appName=Prueba"

mongo=PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        print(email,password)

        user=User(0,'',email,password)

        logged_user=ModelUser.login(mongo,user)

        if logged_user:
            if logged_user.password:
                print('Usuario logueado con exito')
            else:
                print('COntraseña incorrecta')
        else:
            print('Correo invalido')
        

        return render_template('login.html')
    
    elif request.method=='GET':
        return render_template('login.html')
    


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        print(username,email,password)

        user=User(0,username,email,password)

        logged_user=ModelUser.register(mongo,user)

        if logged_user:
            if logged_user.password:
                print('Usuario logueado con exito')
            else:
                print('Contraseña incorrecta')
        else:
            print('Usuario existe')
        

        return render_template('register.html')
    
    elif request.method=='GET':
        return render_template('register.html')



if __name__=='__main__':
    app.run(debug=True)
