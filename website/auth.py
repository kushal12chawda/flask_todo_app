from flask import Blueprint,render_template,request,flash,redirect,url_for
from . import db
from .models import User
from flask_login import login_user, login_required,logout_user,current_user,LoginManager
import bcrypt



auth = Blueprint('auth',__name__)

@auth.route("/")
def login_get_user():
    return render_template("login.html")


@auth.route('/signup',methods=['GET','POST'])
def signup():
    return render_template("Register.html")    

@auth.route('/user/login',methods=['GET','POST'])
def login_post_user():
    try:
        if request.method == 'POST':
            user_name = request.form['username']
            user_password = request.form['password']

          
            user = User.query.filter_by( user_name = user_name).first()
       
            
            if (user):
                print("work")
                if bcrypt.checkpw(user_password.encode('utf-8'),user.user_password):
                    login_user(user,remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash("Incorrect Password ❌")
            else:
                flash("User does not Exists, SIGN IN !!!") 
    except:
        flash("Something went wrong, please TRY AGAIN.")
        return redirect(url_for('views.login_failed'))

    return render_template("login.html")

@auth.route('/user/signup', methods=['GET', 'POST'])
def signup_user():
    try:
        if request.method == 'POST':
            user_name = request.form.get('username')
            user_email = request.form.get('email')
            user_password = request.form.get('password')
            
            if len(user_name) < 3:
                flash('Username cannot be less than 3 characters', category='error')
            elif len(user_password) < 5:
                flash('Password must be greater than 5 characters', category='error')
            else:
                hash = bcrypt.hashpw(user_password.encode('utf-8'),bcrypt.gensalt())
                print(hash)
                new_user = User(user_name = user_name, user_email = user_email, user_password = hash)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created Successfully ✅', category='success')
                return redirect(url_for('views.sign_up_success')) 
    except:
        flash('Either USERNAME or EMAIL already exists, please TRY AGAIN.')
        return redirect(url_for('views.signup_failed'))           

    return render_template("Register.html" , user=current_user) 

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You have been Logged out from our APPLICATION.', category='success')
    return redirect(url_for('auth.login_get_user'))   
