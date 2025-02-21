from flask import Flask,request,render_template,jsonify,flash,redirect,url_for,flash
from flask_login import current_user,login_user,logout_user,LoginManager,login_required
from flask_pymongo import PyMongo
from models.entities.user import User
from models.modeluser import ModelUser
from werkzeug.security import generate_password_hash
from bson import ObjectId
from forms import Login,Register,Objeto


app=Flask(__name__)
app.config['MONGO_URI']="mongodb+srv://david:david@prueba.7tbag.mongodb.net/flaskexamendwes?retryWrites=true&w=majority&appName=Prueba"
app.secret_key='54d8c25705340f53e8b0f081fe49b8fc4285a4d3d1c6446b'
#jwt_secret_key="54d8c25705340f53e8b0f081fe49b8fc428ru333d1c6446b"
mongo=PyMongo(app)


def status_404(error):
    return render_template('error_404.html')

def status_401(error):
    return redirect(url_for('index'))

app.register_error_handler(404,status_404)
app.register_error_handler(401,status_401)


login_manager=LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return ModelUser.get_by_id(mongo,ObjectId(id))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():

    form=Login()

    if form.validate() and request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        print(email,password)

        user=User(0,'',email,password)

        logged_user=ModelUser.login(mongo,user)

        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                flash('Usuario logueado con exito')
                return redirect(url_for('perfil'))
            else:
                flash('COntraseña incorrecta')
                return render_template('login.html',form=form)
        else:
            flash('Correo invalido')
            return render_template('login.html',form=form)
        
    
    else:
        if current_user.is_authenticated:
            return redirect(url_for('perfil'))
        else:
            return render_template('login.html',form=form)
    


@app.route('/register',methods=['GET','POST'])
def register():
    form=Register()

    if form.validate() and request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        print(username,email,password)

        user=User(0,username,email,password)

        logged_user=ModelUser.register(mongo,user)

        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                flash('Usuario logueado con exito')
                return redirect(url_for('perfil'))
            else:
                flash('Contraseña incorrecta')
                print('Contraseña incorrecta')
                return render_template('register.html', form=form)
        else:
            flash('Usuario existe')
            print('Usuario ya existe')
            return render_template('register.html', form=form)
        

    
    else:
        if current_user.is_authenticated:
            return redirect(url_for('perfil'))
        else:
            return render_template('register.html',form=form)



@app.route('/perfil')
@login_required
def perfil():

    objetos=list(mongo.db.objetos.find({"id_user":current_user.id}))
    print('Tus objetos',objetos)

    return render_template('perfil.html',objetos=objetos)



@app.route('/crear',methods=['GET','POST'])
@login_required
def crear():
    form=Objeto()
    
    if form.validate() and request.method=='POST':
        foto=request.form.get('foto')
        descripcion=request.form.get('descripcion')

        print(foto,descripcion)

        mongo.db.objetos.insert_one({"foto":foto,"descripcion":descripcion,"id_user":current_user.id})

        print('Objetos creados')

        return redirect(url_for('perfil'))
    
    else:
        return render_template('crear.html',form=form)
    


@app.route('/edit/<id>',methods=['GET','POST'])
def editar(id):
    form=Objeto()

    if form.validate() and request.method=='POST':
        foto=request.form.get('foto')
        descripcion=request.form.get('descripcion')

        print(foto,descripcion)

        mongo.db.objetos.update_one({"_id":ObjectId(id)},{"$set":{"foto":foto,"descripcion":descripcion}})

        return redirect(url_for('perfil'))
    elif request.method=='GET':
        objeto=mongo.db.objetos.find_one({"_id":ObjectId(id)})
        print(objeto)

        foto=objeto["foto"]
        descripcion=objeto["descripcion"]

        print(foto,descripcion)

        form.foto.data=foto
        form.descripcion.data=descripcion

        return render_template('editar.html',form=form,id=id)
    


@app.route('/delete/<id>',methods=['GET','POST'])
def delete_one(id):
    mongo.db.objetos.delete_one({"_id":ObjectId(id)})
    print('Eliminado ocn exito')

    return redirect(url_for('perfil'))








@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__=='__main__':
    app.run(debug=True)
