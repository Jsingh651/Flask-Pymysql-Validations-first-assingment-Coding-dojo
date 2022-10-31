from flask_app import app
from flask import session, redirect, request, render_template
from flask_app.models.users import User

@app.route('/')
def index ():
    return render_template('register.html')


@app.route('/create/user',methods = ['POST'])
def createuser():
        if not User.validate_users(request.form):
            if request.method == "POST":
                session["first_name"] = request.form.get("first_name")
                session['last_name'] = request.form.get('last_name')
                session['email'] = request.form.get('email')
            return redirect('/')
        data = request.form
        User.create_user(data)
        return redirect('/home')

@app.route('/home')
def showuser():
    users = User.get_all()
    return render_template('users.html',users = users)


