from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, Date, text, literal
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email
from datetime import date
import os
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '1145'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/TrackerSite/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invald Email'), Length(max=50)])
    fullname = StringField('fullname', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

friends = db.Table('friends',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    friends = db.relationship('User', secondary=friends,
                              primaryjoin=(friends.c.user_id == id),
                              secondaryjoin=(friends.c.friend_id == id),
                              backref=db.backref('friend_of', lazy='dynamic'),
                              lazy='dynamic')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class DominionGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class CatanGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class LordsofWaterdeepGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50))
    thirdScore = db.Column(db.Integer)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class CoupGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    winnerName = db.Column(db.String(50), nullable=False)
    cardsLeft = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    thirdName = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    sixthName = db.Column(db.String(50))
    date = db.Column(db.Date)

class LoveLetterGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    winnerName = db.Column(db.String(50), nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    thirdName = db.Column(db.String(50))
    fourthName = db.Column(db.String(50))
    fifthName = db.Column(db.String(50))
    sixthName = db.Column(db.String(50))
    date = db.Column(db.Date)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invald Email'), Length(max=50)])
    fullname = StringField('display name', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
@app.route('/home')
@login_required
def home():
    user = User.query.filter_by(username=current_user.username).first()
    user_friends = user.friends.limit(5).all()

    print(current_user.username)
    print(current_user.fullname)

    # recent_games = basicGame.query.filter(or_(
    #     basicGame.winnerName == current_user.fullname,
    #     basicGame.secondName == current_user.fullname,
    #     basicGame.thirdName == current_user.fullname,
    #     basicGame.winnerName == current_user.username,
    #     basicGame.secondName == current_user.username,
    #     basicGame.thirdName == current_user.username,
    # )).order_by(basicGame.game_id.desc()).limit(5).all()

    # for game in recent_games:
    #     if game.winnerName == current_user.username:
    #         game.winnerName = current_user.fullname
    #     if game.secondName == current_user.username:
    #         game.secondName = current_user.fullname
    #     if game.thirdName == current_user.username:
    #         game.thirdName = current_user.fullname

    # print("recent")
    # print(recent_games)

    dominion_games = DominionGame.query.filter(or_(
        DominionGame.winnerName == current_user.fullname,
        DominionGame.secondName == current_user.fullname,
        DominionGame.thirdName == current_user.fullname,
        DominionGame.fourthName == current_user.fullname,
        DominionGame.winnerName == current_user.username,
        DominionGame.secondName == current_user.username,
        DominionGame.thirdName == current_user.username,
        DominionGame.fourthName == current_user.username
    )).with_entities(DominionGame.game_id, DominionGame.winnerName, DominionGame.secondName, DominionGame.thirdName, DominionGame.date, literal('Dominion').label('game_type')).all()

    recentGames = []

    for game in dominion_games:
        new_game = {}
        if game.winnerName == current_user.username:
            new_game['winnerName'] = current_user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == current_user.username:
            new_game['secondName'] = current_user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == current_user.username:
            new_game['thirdName'] = current_user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Dominion'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    catan_games = CatanGame.query.filter(or_(
        CatanGame.winnerName == current_user.fullname,
        CatanGame.secondName == current_user.fullname,
        CatanGame.thirdName == current_user.fullname,
        CatanGame.fourthName == current_user.fullname,
        CatanGame.winnerName == current_user.username,
        CatanGame.secondName == current_user.username,
        CatanGame.thirdName == current_user.username,
        CatanGame.fourthName == current_user.username
    )).with_entities(CatanGame.game_id, CatanGame.winnerName, CatanGame.secondName, CatanGame.thirdName, CatanGame.date, literal('Catan').label('game_type')).all()

    for game in catan_games:
        new_game = {}
        if game.winnerName == current_user.username:
            new_game['winnerName'] = current_user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == current_user.username:
            new_game['secondName'] = current_user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == current_user.username:
            new_game['thirdName'] = current_user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Catan'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    lords_games = LordsofWaterdeepGame.query.filter(or_(
        LordsofWaterdeepGame.winnerName == current_user.fullname,
        LordsofWaterdeepGame.secondName == current_user.fullname,
        LordsofWaterdeepGame.thirdName == current_user.fullname,
        LordsofWaterdeepGame.fourthName == current_user.fullname,
        LordsofWaterdeepGame.winnerName == current_user.username,
        LordsofWaterdeepGame.secondName == current_user.username,
        LordsofWaterdeepGame.thirdName == current_user.username,
        LordsofWaterdeepGame.fourthName == current_user.username
    )).with_entities(LordsofWaterdeepGame.game_id, LordsofWaterdeepGame.winnerName, LordsofWaterdeepGame.secondName, LordsofWaterdeepGame.thirdName, LordsofWaterdeepGame.date, literal('Catan').label('game_type')).all()

    for game in lords_games:
        new_game = {}
        if game.winnerName == current_user.username:
            new_game['winnerName'] = current_user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == current_user.username:
            new_game['secondName'] = current_user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == current_user.username:
            new_game['thirdName'] = current_user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Lords of Waterdeep'
        new_game['current_date'] = date.today()
        recentGames.append(new_game)

    sortedGames = sorted(recentGames, key=lambda x: x['game_id'], reverse=True)
    top5Games = sortedGames[:5]

    return render_template('home.html', title='Home', name=current_user.fullname, friends=user_friends, recentGames=top5Games)

@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is not None and user.password == password:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))

        return '<h1>wtf</h1>'

    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data, fullname = form.fullname.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> new user created</h1>'
    
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    userName = request.args.get('name')

    if userName != 'current':
        user = User.query.filter_by(username=userName).first()
    else:
        user = current_user

    user_friends = user.friends.limit(5).all()

    dominion_games = DominionGame.query.filter(or_(
        DominionGame.winnerName == current_user.fullname,
        DominionGame.secondName == current_user.fullname,
        DominionGame.thirdName == current_user.fullname,
        DominionGame.fourthName == current_user.fullname,
        DominionGame.winnerName == current_user.username,
        DominionGame.secondName == current_user.username,
        DominionGame.thirdName == current_user.username,
        DominionGame.fourthName == current_user.username
    )).with_entities(DominionGame.game_id, DominionGame.winnerName, DominionGame.secondName, DominionGame.thirdName, DominionGame.date, literal('Dominion').label('game_type')).all()

    recentGames = []

    for game in dominion_games:
        new_game = {}
        if game.winnerName == current_user.username:
            new_game['winnerName'] = current_user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == current_user.username:
            new_game['secondName'] = current_user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == current_user.username:
            new_game['thirdName'] = current_user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Dominion'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    catan_games = CatanGame.query.filter(or_(
        CatanGame.winnerName == current_user.fullname,
        CatanGame.secondName == current_user.fullname,
        CatanGame.thirdName == current_user.fullname,
        CatanGame.fourthName == current_user.fullname,
        CatanGame.winnerName == current_user.username,
        CatanGame.secondName == current_user.username,
        CatanGame.thirdName == current_user.username,
        CatanGame.fourthName == current_user.username
    )).with_entities(CatanGame.game_id, CatanGame.winnerName, CatanGame.secondName, CatanGame.thirdName, CatanGame.date, literal('Catan').label('game_type')).all()

    for game in catan_games:
        new_game = {}
        if game.winnerName == current_user.username:
            new_game['winnerName'] = current_user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == current_user.username:
            new_game['secondName'] = current_user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == current_user.username:
            new_game['thirdName'] = current_user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Catan'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    lords_games = LordsofWaterdeepGame.query.filter(or_(
        LordsofWaterdeepGame.winnerName == current_user.fullname,
        LordsofWaterdeepGame.secondName == current_user.fullname,
        LordsofWaterdeepGame.thirdName == current_user.fullname,
        LordsofWaterdeepGame.fourthName == current_user.fullname,
        LordsofWaterdeepGame.winnerName == current_user.username,
        LordsofWaterdeepGame.secondName == current_user.username,
        LordsofWaterdeepGame.thirdName == current_user.username,
        LordsofWaterdeepGame.fourthName == current_user.username
    )).with_entities(LordsofWaterdeepGame.game_id, LordsofWaterdeepGame.winnerName, LordsofWaterdeepGame.secondName, LordsofWaterdeepGame.thirdName, LordsofWaterdeepGame.date, literal('Catan').label('game_type')).all()

    for game in lords_games:
        new_game = {}
        if game.winnerName == current_user.username:
            new_game['winnerName'] = current_user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == current_user.username:
            new_game['secondName'] = current_user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == current_user.username:
            new_game['thirdName'] = current_user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Lords of Waterdeep'
        new_game['current_date'] = date.today()
        recentGames.append(new_game)

    sortedGames = sorted(recentGames, key=lambda x: x['game_id'], reverse=True)
    top5Games = sortedGames[:5]

    
    return render_template('profile.html', user=user, friends=user_friends, recentGames = top5Games)

@app.route('/friend', methods = ['GET'])
@login_required
def friend():
    user = current_user
    user_friends = user.friends.all()
    return render_template('friends.html', friends=user_friends)

@app.route('/addfriend', methods=['POST'])
@login_required
def addFriend():
    user1 = current_user
    username = request.form.get('addAccount')
    user2 = User.query.filter_by(username=username).first()

    if user2:
        user1.friends.append(user2)
        user2.friends.append(user1)
        db.session.commit()
        flash('Friend added successfully!', 'success')
    else:
        flash('User not found.', 'danger')

    return redirect(url_for('home'))
        
@app.route('/removefriend', methods=['POST'])
@login_required
def removefriend():
    user1 = current_user
    username = request.form.get('addAccount')
    user2 = User.query.filter_by(username=username).first()

    if user2:
        user1.friends.remove(user2)
        user2.friends.remove(user1)
    return redirect(url_for('friends'))

@app.route('/showGames', methods=['GET'])
@login_required
def showGames():

    Dominiondata = DominionGame.query.filter(or_(
        DominionGame.winnerName == current_user.fullname,
        DominionGame.secondName == current_user.fullname,
        DominionGame.thirdName == current_user.fullname,
        DominionGame.fourthName == current_user.fullname,
        DominionGame.winnerName == current_user.username,
        DominionGame.secondName == current_user.username,
        DominionGame.thirdName == current_user.username,
        DominionGame.fourthName == current_user.username
    )).all()

    for game in Dominiondata:
        if game.winnerName == current_user.username:
            game.winnerName = current_user.fullname
        if game.secondName == current_user.username:
            game.secondName = current_user.fullname
        if game.thirdName == current_user.username:
            game.thirdName = current_user.fullname
        if game.fourthName == current_user.username:
            game.fourthName = current_user.fullname

    Catandata = CatanGame.query.filter(or_(
        CatanGame.winnerName == current_user.fullname,
        CatanGame.secondName == current_user.fullname,
        CatanGame.thirdName == current_user.fullname,
        CatanGame.fourthName == current_user.fullname,
        CatanGame.winnerName == current_user.username,
        CatanGame.secondName == current_user.username,
        CatanGame.thirdName == current_user.username,
        CatanGame.fourthName == current_user.username
    )).all()

    for game in Catandata:
        if game.winnerName == current_user.username:
            game.winnerName = current_user.fullname
        if game.secondName == current_user.username:
            game.secondName = current_user.fullname
        if game.thirdName == current_user.username:
            game.thirdName = current_user.fullname
        if game.fourthName == current_user.username:
            game.fourthName = current_user.fullname
    
    LordsofWaterdeepdata = LordsofWaterdeepGame.query.filter(or_(
        LordsofWaterdeepGame.winnerName == current_user.fullname,
        LordsofWaterdeepGame.secondName == current_user.fullname,
        LordsofWaterdeepGame.thirdName == current_user.fullname,
        LordsofWaterdeepGame.fourthName == current_user.fullname,
        LordsofWaterdeepGame.fifthName == current_user.fullname,
        LordsofWaterdeepGame.winnerName == current_user.username,
        LordsofWaterdeepGame.secondName == current_user.username,
        LordsofWaterdeepGame.thirdName == current_user.username,
        LordsofWaterdeepGame.fourthName == current_user.username,
        LordsofWaterdeepGame.fifthName == current_user.username
    )).all()

    for game in LordsofWaterdeepdata:
        if game.winnerName == current_user.username:
            game.winnerName = current_user.fullname
        if game.secondName == current_user.username:
            game.secondName = current_user.fullname
        if game.thirdName == current_user.username:
            game.thirdName = current_user.fullname
        if game.fourthName == current_user.username:
            game.fourthName = current_user.fullname
        if game.fifthName == current_user.username:
            game.fifthName = current_user.fullname

    Coupdata = CoupGame.query.filter(or_(
        CoupGame.winnerName == current_user.fullname,
        CoupGame.secondName == current_user.fullname,
        CoupGame.thirdName == current_user.fullname,
        CoupGame.fourthName == current_user.fullname,
        CoupGame.fifthName == current_user.fullname,
        CoupGame.sixthName == current_user.fullname,
        CoupGame.winnerName == current_user.username,
        CoupGame.secondName == current_user.username,
        CoupGame.thirdName == current_user.username,
        CoupGame.fourthName == current_user.username,
        CoupGame.fifthName == current_user.username,
        CoupGame.sixthName == current_user.username
    )).all()

    for game in Coupdata:
        if game.winnerName == current_user.username:
            game.winnerName = current_user.fullname
        if game.secondName == current_user.username:
            game.secondName = current_user.fullname
        if game.thirdName == current_user.username:
            game.thirdName = current_user.fullname
        if game.fourthName == current_user.username:
            game.fourthName = current_user.fullname
        if game.fifthName == current_user.username:
            game.fifthName = current_user.fullname
        if game.sixthName == current_user.username:
            game.sixthName = current_user.fullname

    LoveLetterdata = LoveLetterGame.query.filter(or_(
        LoveLetterGame.winnerName == current_user.fullname,
        LoveLetterGame.secondName == current_user.fullname,
        LoveLetterGame.thirdName == current_user.fullname,
        LoveLetterGame.fourthName == current_user.fullname,
        LoveLetterGame.fifthName == current_user.fullname,
        LoveLetterGame.sixthName == current_user.fullname,
        LoveLetterGame.winnerName == current_user.username,
        LoveLetterGame.secondName == current_user.username,
        LoveLetterGame.thirdName == current_user.username,
        LoveLetterGame.fourthName == current_user.username,
        LoveLetterGame.fifthName == current_user.username,
        LoveLetterGame.sixthName == current_user.username
    )).all()

    for game in LoveLetterdata:
        if game.winnerName == current_user.username:
            game.winnerName = current_user.fullname
        if game.secondName == current_user.username:
            game.secondName = current_user.fullname
        if game.thirdName == current_user.username:
            game.thirdName = current_user.fullname
        if game.fourthName == current_user.username:
            game.fourthName = current_user.fullname
        if game.fifthName == current_user.username:
            game.fifthName = current_user.fullname
        if game.sixthName == current_user.username:
            game.sixthName = current_user.fullname

    return render_template('GameRecords.html', title='Home', Dominiondata=Dominiondata, Catandata=Catandata, LordsofWaterdeepdata=LordsofWaterdeepdata, Coupdata=Coupdata, LoveLetterdata=LoveLetterdata)

@app.route('/addGame', methods=['GET'])
@login_required
def addGame():
    return render_template("addGame.html", title='Home')

@app.route('/Dominion', methods = ['GET'])
@login_required
def Dominion():
    return render_template('Dominion.html', title='Home')

@app.route('/addDominion', methods = ['POST', 'GET'])
@login_required
def addDominion():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['Player2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['Player3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['Player4']
            player4Score = request.form['Player4_Score']
            newGameID = findID()
            dominion_game = DominionGame(
                game_id=newGameID, 
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score,
                date=date.today())
            db.session.add(dominion_game)
            db.session.commit()
            print("DominionGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the DominionGame: {e}")

        finally:
            print("Redircting")
            return redirect("http://localhost:5000/DominionAdded")
        
@app.route('/DominionAdded', methods = ['GET'])
@login_required
def DominionAdded():
    gameData = db.session.query(DominionGame).order_by(DominionGame.game_id.desc()).first()
    print(gameData)
    return render_template('DominionOutput.html', title='Home', gameData=gameData)

@app.route('/Catan', methods = ['GET'])
@login_required
def Catan():
    return render_template('Catan.html', title='Home')

@app.route('/addCatan', methods = ['POST', 'GET'])
@login_required
def addCatan():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['Player2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['Player3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['Player4']
            player4Score = request.form['Player4_Score']
            newGameID = findID()
            catan_game = CatanGame(
                game_id=newGameID, 
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score,
                date=date.today())
            db.session.add(catan_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the DominionGame: {e}")

        finally:
            print("Redircting")
            return redirect("http://localhost:5000/CatanAdded")
        
@app.route('/CatanAdded', methods = ['GET'])
@login_required
def CatanAdded():
    gameData = db.session.query(CatanGame).order_by(CatanGame.game_id.desc()).first()
    return render_template('CatanOutput.html', title='Home', gameData=gameData)


@app.route('/LordsofWaterdeep', methods = ['GET'])
@login_required
def LordsofWaterdeep():
    return render_template('LordsofWaterdeep.html', title='Home')

@app.route('/addLordsofWaterdeep', methods = ['POST', 'GET'])
@login_required
def addLordsofWaterdeep():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['Player2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['Player3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['Player4']
            player4Score = request.form['Player4_Score']
            player5 = request.form['Player5']
            player5Score = request.form['Player5_Score']
            newGameID = findID()
            new_game = LordsofWaterdeepGame(
                game_id=newGameID, 
                winnerName=player1, 
                winnerScore=player1Score, 
                secondName=player2, 
                secondScore=player2Score, 
                thirdName=player3, 
                thirdScore=player3Score, 
                fourthName=player4, 
                fourthScore=player4Score, 
                fifthName=player5, 
                fifthScore=player5Score,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        finally:
            print("Redircting")
            return redirect("http://localhost:5000/LordsofWaterdeepAdded")
        
@app.route('/LordsofWaterdeepAdded', methods=['GET'])
@login_required
def LordsofWaterdeepAdded():
    gameData = db.session.query(LordsofWaterdeepGame).order_by(LordsofWaterdeepGame.game_id.desc()).first()
    return render_template('LordsofWaterdeepOutput.html', title='Home', gameData=gameData)

@app.route('/Coup', methods = ['GET'])
@login_required
def Coup():
    return render_template('Coup.html', title='Home')

@app.route('/addCoup', methods = ['POST', 'GET'])
@login_required
def addCoup():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            cardsLeft = request.form['cardsLeft']
            player2 = request.form['Player2']
            player3 = request.form['Player3']
            player4 = request.form['Player4']
            player5 = request.form['Player5']
            player6 = request.form['Player6']
            newGameID = findID()
            new_game = CoupGame(
                game_id=newGameID, 
                winnerName=player1, 
                cardsLeft=cardsLeft, 
                secondName=player2, 
                thirdName=player3, 
                fourthName=player4, 
                fifthName=player5, 
                sixthName=player6,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()
        finally:
            print("Redircting")
            return redirect("http://localhost:5000/CoupAdded")
        
@app.route('/CoupAdded', methods=['GET'])
@login_required
def CoupAdded():
    gameData = db.session.query(CoupGame).order_by(CoupGame.game_id.desc()).first()
    return render_template('CoupOutput.html', title='Home', gameData=gameData)
        
@app.route('/LoveLetter', methods = ['GET'])
def LoveLetter():
    return render_template('LoveLetter.html', title='Home')

@app.route('/addLoveLetter', methods=['POST', 'GET'])
def addLoveLetter():
    if request.method == 'POST':
        player1 = request.form['Player1']
        player2 = request.form['Player2']
        player3 = request.form['Player3']
        player4 = request.form['Player4']
        player5 = request.form['Player5']
        player6 = request.form['Player6']
        newGameID = findID()
        new_game = LoveLetterGame(
            game_id=newGameID, 
            winnerName=player1, 
            secondName=player2, 
            thirdName=player3, 
            fourthName=player4, 
            fifthName=player5, 
            sixthName=player6,
            date=date.today())
        db.session.add(new_game)
        db.session.commit()

        return redirect("/LoveLetterAdded")

@app.route('/LoveLetterAdded', methods=['GET'])
def LoveLetterAdded():
    gameData = db.session.query(LoveLetterGame).order_by(LoveLetterGame.game_id.desc()).all()
    return render_template('LoveLetterOutput.html', title='Home', gameData=gameData)

def findID():
    max_id = db.session.query(db.func.max(DominionGame.game_id)).scalar() or 0
    temp_id = db.session.query(db.func.max(CatanGame.game_id)).scalar() or 0
    max_id = max(max_id, temp_id)
    temp_id = db.session.query(db.func.max(LordsofWaterdeepGame.game_id)).scalar() or 0
    max_id = max(max_id, temp_id)
    temp_id = db.session.query(db.func.max(CoupGame.game_id)).scalar() or 0
    max_id = max(max_id, temp_id)
    #temp_id = db.session.query(db.func.max(LoveLetterGame.game_id)).scalar() or 0
    #max_id = max(max_id, temp_id)

    return max_id + 1