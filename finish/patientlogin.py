from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/g1t6_patient'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

ROLE_CHOICES = [('1', 'Patient')]

class User(UserMixin, db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(255))
    partialnric = db.Column(db.String(15))
    race = db.Column(db.String(15))
    mobileno = db.Column(db.Integer)
    dob = db.Column(db.String(15))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')
    role = SelectField(u'Role', choices=ROLE_CHOICES)
    

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    name = StringField('name', validators=[InputRequired(), Length(min=4, max=25)])
    partialnric = StringField('partialnric', validators=[InputRequired(), Length(min=4, max=15)])
    race = StringField('race', validators=[InputRequired(), Length(min=4, max=15)])
    dob = StringField('dob', validators=[InputRequired(), Length(min=4, max=15)])
    mobileno = StringField('mobileno', validators=[InputRequired(), Length(min=4, max=15)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    getRole = form.role.data
    # Check for roles

    if (getRole == '1'):
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            print(user)
            if user:
                if check_password_hash(user.password, form.password.data):
                # if (user.password==form.password.data):
                    login_user(user, remember=form.remember.data)
                    return redirect(url_for('dashboard'))

            return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, name=form.name.data, partialnric=form.partialnric.data, race=form.race.data, dob=form.dob.data, mobileno=form.mobileno.data)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('/SeekHealth/dashboard.html', name=current_user.name, id=current_user.id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/doctor')
@login_required
def doctor():
    return render_template('/SeekHealth/doctor.html', name=current_user.username, id=current_user.id)

@app.route('/appointment')
@login_required
def appointment():
    return render_template('/SeekHealth/appointment.html', name=current_user.username, id=current_user.id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, debug=True)
