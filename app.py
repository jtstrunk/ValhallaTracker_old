from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_, Date, text, literal
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

userFavorites = db.Table('userFavorites',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('game_id', db.Integer, db.ForeignKey('supported_games.id'))
    )

class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        fullname = db.Column(db.String(50), nullable=False)
        username = db.Column(db.String(15), nullable=False, unique=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(80), nullable=False)

        favorites = db.relationship('SupportedGames', secondary=userFavorites, backref='favoritedby')

        friends = db.relationship('User', secondary=friends,
                                primaryjoin=(friends.c.user_id == id),
                                secondaryjoin=(friends.c.friend_id == id),
                                backref=db.backref('friend_of', lazy='dynamic'),
                                lazy='dynamic')
        
class SupportedGames(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        gameName = db.Column(db.String(50))
        numPlayers = db.Column(db.String(50))

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

class MunchkinGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    winnerName = db.Column(db.String(50), nullable=False)
    winnerScore = db.Column(db.Integer, nullable=False)
    secondName = db.Column(db.String(50), nullable=False)
    secondScore = db.Column(db.Integer, nullable=False)
    thirdName = db.Column(db.String(50), nullable=False)
    thirdScore = db.Column(db.Integer, nullable=False)
    fourthName = db.Column(db.String(50))
    fourthScore = db.Column(db.Integer)
    fifthName = db.Column(db.String(50))
    fifthScore = db.Column(db.Integer)
    sixthName = db.Column(db.String(50))
    sixthScore = db.Column(db.Integer)
    date = db.Column(db.Date)

class TheMindGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    playerone = db.Column(db.String(50), nullable=False)
    playertwo = db.Column(db.String(50), nullable=False)
    playerthree = db.Column(db.String(50))
    playerfour = db.Column(db.String(50))
    victory = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)
    
class JustOneGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    playerone = db.Column(db.String(50), nullable=False)
    playertwo = db.Column(db.String(50), nullable=False)
    playerthree = db.Column(db.String(50))
    playerfour = db.Column(db.String(50))
    playerfive = db.Column(db.String(50))
    playersix = db.Column(db.String(50))
    playerseven = db.Column(db.String(50))
    victory = db.Column(db.Integer, nullable=False)
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

    gamesWon = calcGamesWon(user)
    gamesPlayed = calcGamesPlayed(user)
    mostPlayed = calcMostPlayed(user)
    mostWon = calcMostWon(user)
    bestFriend = calcBestFriend(user)

    profileStats = [gamesPlayed, gamesWon, mostPlayed, mostWon, bestFriend]

    return render_template('home.html', title='Home', name=current_user.fullname, friends=user_friends, recentGames=top5Games, profileStats=profileStats)

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

        

    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data, fullname = form.fullname.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    
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

    print("USER")
    print(user)

    user_friends = user.friends.limit(5).all()
    recentGames = []

    dominion_games = DominionGame.query.filter(or_(
        DominionGame.winnerName == user.fullname,
        DominionGame.secondName == user.fullname,
        DominionGame.thirdName == user.fullname,
        DominionGame.fourthName == user.fullname,
        DominionGame.winnerName == user.username,
        DominionGame.secondName == user.username,
        DominionGame.thirdName == user.username,
        DominionGame.fourthName == user.username
    )).with_entities(DominionGame.game_id, DominionGame.winnerName, DominionGame.secondName, DominionGame.thirdName, DominionGame.date, literal('Dominion').label('game_type')).all()

    for game in dominion_games:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Dominion'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    catan_games = CatanGame.query.filter(or_(
        CatanGame.winnerName == user.fullname,
        CatanGame.secondName == user.fullname,
        CatanGame.thirdName == user.fullname,
        CatanGame.fourthName == user.fullname,
        CatanGame.winnerName == user.username,
        CatanGame.secondName == user.username,
        CatanGame.thirdName == user.username,
        CatanGame.fourthName == user.username
    )).with_entities(CatanGame.game_id, CatanGame.winnerName, CatanGame.secondName, CatanGame.thirdName, CatanGame.date, literal('Catan').label('game_type')).all()

    for game in catan_games:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Catan'
        new_game['current_date'] = game.date
        recentGames.append(new_game)

    lords_games = LordsofWaterdeepGame.query.filter(or_(
        LordsofWaterdeepGame.winnerName == user.fullname,
        LordsofWaterdeepGame.secondName == user.fullname,
        LordsofWaterdeepGame.thirdName == user.fullname,
        LordsofWaterdeepGame.fourthName == user.fullname,
        LordsofWaterdeepGame.winnerName == user.username,
        LordsofWaterdeepGame.secondName == user.username,
        LordsofWaterdeepGame.thirdName == user.username,
        LordsofWaterdeepGame.fourthName == user.username
    )).with_entities(LordsofWaterdeepGame.game_id, LordsofWaterdeepGame.winnerName, LordsofWaterdeepGame.secondName, LordsofWaterdeepGame.thirdName, LordsofWaterdeepGame.date, literal('Catan').label('game_type')).all()

    for game in lords_games:
        new_game = {}
        if game.winnerName == user.username:
            new_game['winnerName'] = user.fullname
        else:
            new_game['winnerName'] = game.winnerName
        if game.secondName == user.username:
            new_game['secondName'] = user.fullname
        else:
            new_game['secondName'] = game.secondName
        if game.thirdName == user.username:
            new_game['thirdName'] = user.fullname
        else:
            new_game['thirdName'] = game.thirdName

        new_game['game_id'] = game.game_id
        new_game['game_type'] = 'Lords of Waterdeep'
        new_game['current_date'] = date.today()
        recentGames.append(new_game)

    sortedGames = sorted(recentGames, key=lambda x: x['game_id'], reverse=True)
    top5Games = sortedGames[:5]

    # user_id = user.id
    # user = User.query.filter_by(id=user_id).first()
    games = user.favorites

    gameResults = []
    for game in games:
        #fullname = user.fullname
        game_name = game.gameName
        num_players = game.numPlayers
        gameResults.append((game_name, num_players))

    print(gameResults)

    for game_name, num_players in gameResults:
        print(f"{game_name} has {num_players}")

    gamesWon = calcGamesWon(user)
    gamesPlayed = calcGamesPlayed(user)
    mostPlayed = calcMostPlayed(user)
    mostWon = calcMostWon(user)
    bestFriend = calcBestFriend(user)
    
    profileStats = [gamesPlayed, gamesWon, mostPlayed, mostWon, bestFriend]

    
    return render_template('profile.html', user=user, friends=user_friends, recentGames = top5Games, favoriteGames=gameResults, profileStats = profileStats, profileName=userName, currUser = current_user)

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
    username = request.form.get('removeAccount')
    user2 = User.query.filter_by(username=username).first()

    if user2:
        user1.friends.remove(user2)
        user2.friends.remove(user1)
        db.session.commit()
        print("removingdasdsadsadsa")

    print("removing")
    return redirect(url_for('friend'))

@app.route('/addFavorite', methods=['POST'])
def addFavorite():
    game = request.args.get('game')
    print(game)
    user = User.query.get(current_user.id)
    # gameID = 4
    game_obj = SupportedGames.query.filter_by(gameName=game).first()
    user.favorites.append(game_obj)

    # favorite = userFavorites(user_id=userID, game_id=gameID)
    # userID.favorites.append(favorite)
    db.session.commit()
    return 'Game Added'


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

@app.route('/addDominion', methods = ['POST', 'GET'])
@login_required
def addDominion():
    if request.method == 'POST':
        try:
            player1 = request.form['dominionPlayer1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['dominionPlayer2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['dominionPlayer3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['dominionPlayer4']
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
            print("Record Added")
            return redirect('/addGame')

@app.route('/addCatan', methods = ['POST', 'GET'])
@login_required
def addCatan():
    if request.method == 'POST':
        try:
            player1 = request.form['catanPlayer1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['catanPlayer2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['catanPlayer3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['catanPlayer4']
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
            print(f"An error occurred while adding the CatanGame: {e}")

        finally:
            print("Record Added")
            return redirect('/addGame')

@app.route('/addLordsofWaterdeep', methods = ['POST', 'GET'])
@login_required
def addLordsofWaterdeep():
    if request.method == 'POST':
        try:
            player1 = request.form['lordsofwaterdeepPlayer1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['lordsofwaterdeepPlayer2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['lordsofwaterdeepPlayer3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['lordsofwaterdeepPlayer4']
            player4Score = request.form['Player4_Score']
            player5 = request.form['lordsofwaterdeepPlayer5']
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

        except Exception as e:
            print(f"An error occurred while adding the LordsofWaterdeepGame: {e}")

        finally:
            print("Record Added")
            return redirect('/addGame')
        
@app.route('/addCoup', methods = ['POST', 'GET'])
@login_required
def addCoup():
    if request.method == 'POST':
        try:
            player1 = request.form['coupPlayer1']
            player2 = request.form['coupPlayer2']
            player3 = request.form['coupPlayer3']
            player4 = request.form['coupPlayer4']
            player5 = request.form['coupPlayer5']
            player6 = request.form['coupPlayer6']
            newGameID = findID()
            new_game = CoupGame(
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

        except Exception as e:
            print(f"An error occurred while adding the CoupGame: {e}")

        finally:
            print("Record Added")
            return redirect('/addGame')
        
@app.route('/addLoveLetter', methods=['POST', 'GET'])
def addLoveLetter():
    if request.method == 'POST':
        try:
            player1 = request.form['loveletterPlayer1']
            player2 = request.form['loveletterPlayer2']
            player3 = request.form['loveletterPlayer3']
            player4 = request.form['loveletterPlayer4']
            player5 = request.form['loveletterPlayer5']
            player6 = request.form['loveletterPlayer6']
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

        finally:
            print("Record Added")
            return redirect('/addGame')
        
@app.route('/addMunchkin', methods = ['POST', 'GET'])
@login_required
def addMunchkin():
    if request.method == 'POST':
        try:
            player1 = request.form['munchkinPlayer1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['munchkinPlayer2']
            player2Score = request.form['Player2_Score']
            player3 = request.form['munchkinPlayer3']
            player3Score = request.form['Player3_Score']
            player4 = request.form['munchkinPlayer4']
            player4Score = request.form['Player4_Score']
            player5 = request.form['munchkinPlayer5']
            player5Score = request.form['Player5_Score']
            player6 = request.form['munchkinPlayer6']
            player6Score = request.form['Player6_Score']
            newGameID = findID()
            new_game = MunchkinGame(
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
                sixthName=player6, 
                sixthScore=player6Score,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()

        except Exception as e:
            print(f"An error occurred while adding the MunchkinGame: {e}")

        finally:
            print("Record Added")
            return redirect('/addGame')
        
@app.route('/addJustOne', methods = ['POST', 'GET'])
@login_required
def addJustOne():
    if request.method == 'POST':
        try:
            player1 = request.form['justonePlayer1']
            player2 = request.form['justonePlayer2']
            player3 = request.form['justonePlayer3']
            player4 = request.form['justonePlayer4']
            player5 = request.form['justonePlayer5']
            player6 = request.form['justonePlayer6']
            player7 = request.form['justonePlayer7']
            gamevictory = request.form['win']
            newGameID = findID()
            new_game = JustOneGame(
                game_id=newGameID, 
                playerone=player1, 
                playertwo=player2,  
                playerthree=player3, 
                playerfour=player4,
                playerfive=player5,  
                playersix=player6, 
                playerseven=player7,  
                victory = gamevictory,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()
            print("JustOneGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the JustOneGame: {e}")

        finally:
            print("Record Added")
            return redirect('/addGame')
        
@app.route('/addTheMind', methods = ['POST', 'GET'])
@login_required
def addTheMind():
    if request.method == 'POST':
        try:
            player1 = request.form['themindPlayer1']
            player2 = request.form['themindPlayer2']
            player3 = request.form['themindPlayer3']
            player4 = request.form['themindPlayer4']
            gamevictory = request.form['win']
            newGameID = findID()
            new_game = TheMindGame(
                game_id=newGameID, 
                playerone=player1, 
                playertwo=player2,  
                playerthree=player3, 
                playerfour=player4, 
                victory = gamevictory,
                date=date.today())
            db.session.add(new_game)
            db.session.commit()
            print("TheMindGame added successfully!")

        except Exception as e:
            print(f"An error occurred while adding the TheMindGame: {e}")

        finally:
            print("Record Added")
            return redirect('/addGame')

def findID():
    dom_id = db.session.query(db.func.max(DominionGame.game_id)).scalar() or 0
    cat_id = db.session.query(db.func.max(CatanGame.game_id)).scalar() or 0
    lor_id = db.session.query(db.func.max(LordsofWaterdeepGame.game_id)).scalar() or 0
    cou_id = db.session.query(db.func.max(CoupGame.game_id)).scalar() or 0
    lov_id = db.session.query(db.func.max(LoveLetterGame.game_id)).scalar() or 0
    mun_id = db.session.query(db.func.max(MunchkinGame.game_id)).scalar() or 0
    jus_id = db.session.query(db.func.max(JustOneGame.game_id)).scalar() or 0
    min_id = db.session.query(db.func.max(TheMindGame.game_id)).scalar() or 0
    max_id = max(dom_id, cat_id, lor_id, cou_id, lov_id, mun_id, jus_id, min_id)

    return max_id + 1

def calcGamesWon(user):
    gamesWon = 0
    gamesWon += db.session.query(DominionGame).filter(or_(DominionGame.winnerName == user.username, DominionGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(CatanGame).filter(or_(CatanGame.winnerName == user.username, CatanGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(LordsofWaterdeepGame).filter(or_(LordsofWaterdeepGame.winnerName == user.username, LordsofWaterdeepGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(CoupGame).filter(or_(CoupGame.winnerName == user.username, CoupGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(LoveLetterGame).filter(or_(LoveLetterGame.winnerName == user.username, LoveLetterGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(MunchkinGame).filter(or_(MunchkinGame.winnerName == user.username, MunchkinGame.winnerName == user.fullname)).count()
    gamesWon += db.session.query(TheMindGame).filter(
        and_(
            TheMindGame.victory == 'Yes',
            or_(
                TheMindGame.playerone == user.username,
                TheMindGame.playerone == user.fullname,
                TheMindGame.playertwo == user.username,
                TheMindGame.playertwo == user.fullname,
                TheMindGame.playerthree == user.username,
                TheMindGame.playerthree == user.fullname,
                TheMindGame.playerfour == user.username,
                TheMindGame.playerfour == user.fullname,
            )
        )
    ).count()

    return gamesWon

def calcGamesPlayed(user):
    gamesPlayed = 0
    gamesPlayed += db.session.query(DominionGame).filter(or_(
        DominionGame.winnerName == user.fullname,
        DominionGame.secondName == user.fullname,
        DominionGame.thirdName == user.fullname,
        DominionGame.fourthName == user.fullname,
        DominionGame.winnerName == user.username,
        DominionGame.secondName == user.username,
        DominionGame.thirdName == user.username,
        DominionGame.fourthName == user.username)).count()
    gamesPlayed += db.session.query(CatanGame).filter(or_(
        CatanGame.winnerName == user.fullname,
        CatanGame.secondName == user.fullname,
        CatanGame.thirdName == user.fullname,
        CatanGame.fourthName == user.fullname,
        CatanGame.winnerName == user.username,
        CatanGame.secondName == user.username,
        CatanGame.thirdName == user.username,
        CatanGame.fourthName == user.username)).count()
    gamesPlayed += db.session.query(LordsofWaterdeepGame).filter(or_(
        LordsofWaterdeepGame.winnerName == user.fullname,
        LordsofWaterdeepGame.secondName == user.fullname,
        LordsofWaterdeepGame.thirdName == user.fullname,
        LordsofWaterdeepGame.fourthName == user.fullname,
        LordsofWaterdeepGame.fifthName == user.fullname,
        LordsofWaterdeepGame.winnerName == user.username,
        LordsofWaterdeepGame.secondName == user.username,
        LordsofWaterdeepGame.thirdName == user.username,
        LordsofWaterdeepGame.fourthName == user.username,
        LordsofWaterdeepGame.fifthName == user.username)).count()
    gamesPlayed += db.session.query(CoupGame).filter(or_(
        CoupGame.winnerName == user.fullname,
        CoupGame.secondName == user.fullname,
        CoupGame.thirdName == user.fullname,
        CoupGame.fourthName == user.fullname,
        CoupGame.fifthName == user.fullname,
        CoupGame.sixthName == user.fullname,
        CoupGame.winnerName == user.username,
        CoupGame.secondName == user.username,
        CoupGame.thirdName == user.username,
        CoupGame.fourthName == user.username,
        CoupGame.fifthName == user.username,
        CoupGame.sixthName == user.username)).count()
    gamesPlayed += db.session.query(LoveLetterGame).filter(or_(
        LoveLetterGame.winnerName == user.fullname,
        LoveLetterGame.secondName == user.fullname,
        LoveLetterGame.thirdName == user.fullname,
        LoveLetterGame.fourthName == user.fullname,
        LoveLetterGame.fifthName == user.fullname,
        LoveLetterGame.sixthName == user.fullname,
        LoveLetterGame.winnerName == user.username,
        LoveLetterGame.secondName == user.username,
        LoveLetterGame.thirdName == user.username,
        LoveLetterGame.fourthName == user.username,
        LoveLetterGame.fifthName == user.username,
        LoveLetterGame.sixthName == user.username)).count()
    gamesPlayed += db.session.query(MunchkinGame).filter(or_(
        MunchkinGame.winnerName == user.fullname,
        MunchkinGame.secondName == user.fullname,
        MunchkinGame.thirdName == user.fullname,
        MunchkinGame.fourthName == user.fullname,
        MunchkinGame.fifthName == user.fullname,
        MunchkinGame.sixthName == user.fullname,
        MunchkinGame.winnerName == user.username,
        MunchkinGame.secondName == user.username,
        MunchkinGame.thirdName == user.username,
        MunchkinGame.fourthName == user.username,
        MunchkinGame.fifthName == user.username,
        MunchkinGame.sixthName == user.username)).count()
    gamesPlayed += db.session.query(TheMindGame).filter(or_(
        TheMindGame.playerone == user.fullname,
        TheMindGame.playertwo == user.fullname,
        TheMindGame.playerthree == user.fullname,
        TheMindGame.playerfour == user.fullname,
        TheMindGame.playerone == user.username,
        TheMindGame.playertwo == user.username,
        TheMindGame.playerthree == user.username,
        TheMindGame.playerfour == user.username)).count()
    gamesPlayed += db.session.query(JustOneGame).filter(or_(
        JustOneGame.playerone == user.fullname,
        JustOneGame.playertwo == user.fullname,
        JustOneGame.playerthree == user.fullname,
        JustOneGame.playerfour == user.fullname,
        JustOneGame.playerfive == user.fullname,
        JustOneGame.playersix == user.fullname,
        JustOneGame.playerseven == user.fullname,
        JustOneGame.playerone == user.username,
        JustOneGame.playertwo == user.username,
        JustOneGame.playerthree == user.username,
        JustOneGame.playerfour == user.username,
        JustOneGame.playerfive == user.username,
        JustOneGame.playersix == user.username,
        JustOneGame.playerseven == user.username)).count()

    return gamesPlayed

def calcMostPlayed(user):
    mostPlayed = ""

    DominionCount = db.session.query(DominionGame).filter(or_(
        DominionGame.winnerName == user.fullname,
        DominionGame.secondName == user.fullname,
        DominionGame.thirdName == user.fullname,
        DominionGame.fourthName == user.fullname,
        DominionGame.winnerName == user.username,
        DominionGame.secondName == user.username,
        DominionGame.thirdName == user.username,
        DominionGame.fourthName == user.username)).count()
    CatanCount = db.session.query(CatanGame).filter(or_(
        CatanGame.winnerName == user.fullname,
        CatanGame.secondName == user.fullname,
        CatanGame.thirdName == user.fullname,
        CatanGame.fourthName == user.fullname,
        CatanGame.winnerName == user.username,
        CatanGame.secondName == user.username,
        CatanGame.thirdName == user.username,
        CatanGame.fourthName == user.username)).count()
    LordsofWaterdeepCount = db.session.query(LordsofWaterdeepGame).filter(or_(
        LordsofWaterdeepGame.winnerName == user.fullname,
        LordsofWaterdeepGame.secondName == user.fullname,
        LordsofWaterdeepGame.thirdName == user.fullname,
        LordsofWaterdeepGame.fourthName == user.fullname,
        LordsofWaterdeepGame.fifthName == user.fullname,
        LordsofWaterdeepGame.winnerName == user.username,
        LordsofWaterdeepGame.secondName == user.username,
        LordsofWaterdeepGame.thirdName == user.username,
        LordsofWaterdeepGame.fourthName == user.username,
        LordsofWaterdeepGame.fifthName == user.username)).count()
    CoupCount = db.session.query(CoupGame).filter(or_(
        CoupGame.winnerName == user.fullname,
        CoupGame.secondName == user.fullname,
        CoupGame.thirdName == user.fullname,
        CoupGame.fourthName == user.fullname,
        CoupGame.fifthName == user.fullname,
        CoupGame.sixthName == user.fullname,
        CoupGame.winnerName == user.username,
        CoupGame.secondName == user.username,
        CoupGame.thirdName == user.username,
        CoupGame.fourthName == user.username,
        CoupGame.fifthName == user.username,
        CoupGame.sixthName == user.username)).count()
    LoveLetterCount = db.session.query(LoveLetterGame).filter(or_(
        LoveLetterGame.winnerName == user.fullname,
        LoveLetterGame.secondName == user.fullname,
        LoveLetterGame.thirdName == user.fullname,
        LoveLetterGame.fourthName == user.fullname,
        LoveLetterGame.fifthName == user.fullname,
        LoveLetterGame.sixthName == user.fullname,
        LoveLetterGame.winnerName == user.username,
        LoveLetterGame.secondName == user.username,
        LoveLetterGame.thirdName == user.username,
        LoveLetterGame.fourthName == user.username,
        LoveLetterGame.fifthName == user.username,
        LoveLetterGame.sixthName == user.username)).count()
    MunchkinCount = db.session.query(MunchkinGame).filter(or_(
        MunchkinGame.winnerName == user.fullname,
        MunchkinGame.secondName == user.fullname,
        MunchkinGame.thirdName == user.fullname,
        MunchkinGame.fourthName == user.fullname,
        MunchkinGame.fifthName == user.fullname,
        MunchkinGame.sixthName == user.fullname,
        MunchkinGame.winnerName == user.username,
        MunchkinGame.secondName == user.username,
        MunchkinGame.thirdName == user.username,
        MunchkinGame.fourthName == user.username,
        MunchkinGame.fifthName == user.username,
        MunchkinGame.sixthName == user.username)).count()
    TheMindCount = db.session.query(TheMindGame).filter(or_(
        TheMindGame.playerone == user.fullname,
        TheMindGame.playertwo == user.fullname,
        TheMindGame.playerthree == user.fullname,
        TheMindGame.playerfour == user.fullname,
        TheMindGame.playerone == user.username,
        TheMindGame.playertwo == user.username,
        TheMindGame.playerthree == user.username,
        TheMindGame.playerfour == user.username)).count()
    JustOneCount = db.session.query(JustOneGame).filter(or_(
        JustOneGame.playerone == user.fullname,
        JustOneGame.playertwo == user.fullname,
        JustOneGame.playerthree == user.fullname,
        JustOneGame.playerfour == user.fullname,
        JustOneGame.playerfive == user.fullname,
        JustOneGame.playersix == user.fullname,
        JustOneGame.playerseven == user.fullname,
        JustOneGame.playerone == user.username,
        JustOneGame.playertwo == user.username,
        JustOneGame.playerthree == user.username,
        JustOneGame.playerfour == user.username,
        JustOneGame.playerfive == user.username,
        JustOneGame.playersix == user.username,
        JustOneGame.playerseven == user.username)).count()
    
    counts = {
        'DomionionCount': DominionCount,
        'CatanCount': CatanCount,
        'LordsofWaterdeepCount': LordsofWaterdeepCount,
        'CoupCount': CoupCount,
        'LoveLetterCount': LoveLetterCount,
        'MunchkinCount': MunchkinCount,
        'TheMindCount': TheMindCount,
        'JustOneCount': JustOneCount
    }

    maxCount = max(counts.values())
    mostPlayed = [variable for variable, count in counts.items() if count == maxCount]

    return mostPlayed[0][:-5]

def calcMostWon(user):
    dominionWins = db.session.query(DominionGame).filter(or_(DominionGame.winnerName == user.username, DominionGame.winnerName == user.fullname)).count()
    catanWins = db.session.query(CatanGame).filter(or_(CatanGame.winnerName == user.username, CatanGame.winnerName == user.fullname)).count()
    lordsofwaterdeepWins = db.session.query(LordsofWaterdeepGame).filter(or_(LordsofWaterdeepGame.winnerName == user.username, LordsofWaterdeepGame.winnerName == user.fullname)).count()
    coupWins = db.session.query(CoupGame).filter(or_(CoupGame.winnerName == user.username, CoupGame.winnerName == user.fullname)).count()
    loveletterWins = db.session.query(LoveLetterGame).filter(or_(LoveLetterGame.winnerName == user.username, LoveLetterGame.winnerName == user.fullname)).count()
    munchkinWins = db.session.query(MunchkinGame).filter(or_(MunchkinGame.winnerName == user.username, MunchkinGame.winnerName == user.fullname)).count()
    themindWins = db.session.query(TheMindGame).filter(
        and_(
            TheMindGame.victory == 'Yes',
            or_(
                TheMindGame.playerone == user.username,
                TheMindGame.playerone == user.fullname,
                TheMindGame.playertwo == user.username,
                TheMindGame.playertwo == user.fullname,
                TheMindGame.playerthree == user.username,
                TheMindGame.playerthree == user.fullname,
                TheMindGame.playerfour == user.username,
                TheMindGame.playerfour == user.fullname,
            )
        )
    ).count()

    counts = {
        'DomionionCount': dominionWins,
        'CatanCount': catanWins,
        'LordsofWaterdeepCount': lordsofwaterdeepWins,
        'CoupCount': coupWins,
        'LoveLetterCount': loveletterWins,
        'MunchkinCount': munchkinWins,
        'TheMindCount': themindWins
    }

    maxCount = max(counts.values())
    mostWon = [variable for variable, count in counts.items() if count == maxCount]

    return mostWon[0][:-5]

def calcBestFriend(user):
    bestFriend = ""
    maxCount = 0
    user_friends = user.friends.all()

    for friend in user_friends:
        DominionCount = db.session.query(DominionGame).filter(and_(
            or_(
                DominionGame.winnerName == friend.fullname,
                DominionGame.secondName == friend.fullname,
                DominionGame.thirdName == friend.fullname,
                DominionGame.fourthName == friend.fullname,
                DominionGame.winnerName == friend.username,
                DominionGame.secondName == friend.username,
                DominionGame.thirdName == friend.username,
                DominionGame.fourthName == friend.username
            ), or_( 
                DominionGame.winnerName == user.fullname,
                DominionGame.secondName == user.fullname,
                DominionGame.thirdName == user.fullname,
                DominionGame.fourthName == user.fullname,
                DominionGame.winnerName == user.username,
                DominionGame.secondName == user.username,
                DominionGame.thirdName == user.username,
                DominionGame.fourthName == user.username
            ))).count()

        CatanCount = db.session.query(CatanGame).filter(and_(
            or_(
                CatanGame.winnerName == friend.fullname,
                CatanGame.secondName == friend.fullname,
                CatanGame.thirdName == friend.fullname,
                CatanGame.fourthName == friend.fullname,
                CatanGame.winnerName == friend.username,
                CatanGame.secondName == friend.username,
                CatanGame.thirdName == friend.username,
                CatanGame.fourthName == friend.username
            ), or_(
                CatanGame.winnerName == user.fullname,
                CatanGame.secondName == user.fullname,
                CatanGame.thirdName == user.fullname,
                CatanGame.fourthName == user.fullname,
                CatanGame.winnerName == user.username,
                CatanGame.secondName == user.username,
                CatanGame.thirdName == user.username,
                CatanGame.fourthName == user.username
            ))).count()

        LordsofWaterdeepCount = db.session.query(LordsofWaterdeepGame).filter(and_(
            or_(
                LordsofWaterdeepGame.winnerName == friend.fullname,
                LordsofWaterdeepGame.secondName == friend.fullname,
                LordsofWaterdeepGame.thirdName == friend.fullname,
                LordsofWaterdeepGame.fourthName == friend.fullname,
                LordsofWaterdeepGame.fifthName == friend.fullname,
                LordsofWaterdeepGame.winnerName == friend.username,
                LordsofWaterdeepGame.secondName == friend.username,
                LordsofWaterdeepGame.thirdName == friend.username,
                LordsofWaterdeepGame.fourthName == friend.username,
                LordsofWaterdeepGame.fifthName == friend.username
            ), or_(
                LordsofWaterdeepGame.winnerName == user.fullname,
                LordsofWaterdeepGame.secondName == user.fullname,
                LordsofWaterdeepGame.thirdName == user.fullname,
                LordsofWaterdeepGame.fourthName == user.fullname,
                LordsofWaterdeepGame.fifthName == user.fullname,
                LordsofWaterdeepGame.winnerName == user.username,
                LordsofWaterdeepGame.secondName == user.username,
                LordsofWaterdeepGame.thirdName == user.username,
                LordsofWaterdeepGame.fourthName == user.username,
                LordsofWaterdeepGame.fifthName == user.username
            ))).count()

        CoupCount = db.session.query(CoupGame).filter(and_(
            or_(
                CoupGame.winnerName == friend.fullname,
                CoupGame.secondName == friend.fullname,
                CoupGame.thirdName == friend.fullname,
                CoupGame.fourthName == friend.fullname,
                CoupGame.fifthName == friend.fullname,
                CoupGame.sixthName == friend.fullname,
                CoupGame.winnerName == friend.username,
                CoupGame.secondName == friend.username,
                CoupGame.thirdName == friend.username,
                CoupGame.fourthName == friend.username,
                CoupGame.fifthName == friend.username,
                CoupGame.sixthName == friend.username
            ), or_(
                CoupGame.winnerName == user.fullname,
                CoupGame.secondName == user.fullname,
                CoupGame.thirdName == user.fullname,
                CoupGame.fourthName == user.fullname,
                CoupGame.fifthName == user.fullname,
                CoupGame.sixthName == user.fullname,
                CoupGame.winnerName == user.username,
                CoupGame.secondName == user.username,
                CoupGame.thirdName == user.username,
                CoupGame.fourthName == user.username,
                CoupGame.fifthName == user.username,
                CoupGame.sixthName == user.username
            ))).count()

        LoveLetterCount = db.session.query(LoveLetterGame).filter(and_(
            or_(
                LoveLetterGame.winnerName == user.fullname,
                LoveLetterGame.secondName == friend.fullname,
                LoveLetterGame.thirdName == friend.fullname,
                LoveLetterGame.fourthName == friend.fullname,
                LoveLetterGame.fifthName == friend.fullname,
                LoveLetterGame.sixthName == friend.fullname,
                LoveLetterGame.winnerName == friend.username,
                LoveLetterGame.secondName == friend.username,
                LoveLetterGame.thirdName == friend.username,
                LoveLetterGame.fourthName == friend.username,
                LoveLetterGame.fifthName == friend.username,
                LoveLetterGame.sixthName == friend.username),
            or_(
                LoveLetterGame.winnerName == user.fullname,
                LoveLetterGame.secondName == user.fullname,
                LoveLetterGame.thirdName == user.fullname,
                LoveLetterGame.fourthName == user.fullname,
                LoveLetterGame.fifthName == user.fullname,
                LoveLetterGame.sixthName == user.fullname,
                LoveLetterGame.winnerName == user.username,
                LoveLetterGame.secondName == user.username,
                LoveLetterGame.thirdName == user.username,
                LoveLetterGame.fourthName == user.username,
                LoveLetterGame.fifthName == user.username,
                LoveLetterGame.sixthName == user.username))).count()
        
        MunchkinCount = db.session.query(MunchkinGame).filter(and_(
            or_(
                MunchkinGame.winnerName == friend.fullname,
                MunchkinGame.secondName == friend.fullname,
                MunchkinGame.thirdName == friend.fullname,
                MunchkinGame.fourthName == friend.fullname,
                MunchkinGame.fifthName == friend.fullname,
                MunchkinGame.sixthName == friend.fullname,
                MunchkinGame.winnerName == friend.username,
                MunchkinGame.secondName == friend.username,
                MunchkinGame.thirdName == friend.username,
                MunchkinGame.fourthName == friend.username,
                MunchkinGame.fifthName == friend.username,
                MunchkinGame.sixthName == friend.username
            ), or_(
                MunchkinGame.winnerName == user.fullname,
                MunchkinGame.secondName == user.fullname,
                MunchkinGame.thirdName == user.fullname,
                MunchkinGame.fourthName == user.fullname,
                MunchkinGame.fifthName == user.fullname,
                MunchkinGame.sixthName == user.fullname,
                MunchkinGame.winnerName == user.username,
                MunchkinGame.secondName == user.username,
                MunchkinGame.thirdName == user.username,
                MunchkinGame.fourthName == user.username,
                MunchkinGame.fifthName == user.username,
                MunchkinGame.sixthName == user.username
            ))).count()

        TheMindCount = db.session.query(TheMindGame).filter(and_(
            or_(
                TheMindGame.playerone == friend.fullname,
                TheMindGame.playertwo == friend.fullname,
                TheMindGame.playerthree == friend.fullname,
                TheMindGame.playerfour == friend.fullname,
                TheMindGame.playerone == friend.username,
                TheMindGame.playertwo == friend.username,
                TheMindGame.playerthree == friend.username,
                TheMindGame.playerfour == friend.username
            ), or_(
                TheMindGame.playerone == user.fullname,
                TheMindGame.playertwo == user.fullname,
                TheMindGame.playerthree == user.fullname,
                TheMindGame.playerfour == user.fullname,
                TheMindGame.playerone == user.username,
                TheMindGame.playertwo == user.username,
                TheMindGame.playerthree == user.username,
                TheMindGame.playerfour == user.username
            ))).count()

        JustOneCount = db.session.query(JustOneGame).filter(and_(
            or_(
                JustOneGame.playerone == friend.fullname,
                JustOneGame.playertwo == friend.fullname,
                JustOneGame.playerthree == friend.fullname,
                JustOneGame.playerfour == friend.fullname,
                JustOneGame.playerfive == friend.fullname,
                JustOneGame.playersix == friend.fullname,
                JustOneGame.playerseven == friend.fullname,
                JustOneGame.playerone == friend.username,
                JustOneGame.playertwo == friend.username,
                JustOneGame.playerthree == friend.username,
                JustOneGame.playerfour == friend.username,
                JustOneGame.playerfive == friend.username,
                JustOneGame.playersix == friend.username,
                JustOneGame.playerseven == friend.username
            ), or_(
                JustOneGame.playerone == user.fullname,
                JustOneGame.playertwo == user.fullname,
                JustOneGame.playerthree == user.fullname,
                JustOneGame.playerfour == user.fullname,
                JustOneGame.playerfive == user.fullname,
                JustOneGame.playersix == user.fullname,
                JustOneGame.playerseven == user.fullname,
                JustOneGame.playerone == user.username,
                JustOneGame.playertwo == user.username,
                JustOneGame.playerthree == user.username,
                JustOneGame.playerfour == user.username,
                JustOneGame.playerfive == user.username,
                JustOneGame.playersix == user.username,
                JustOneGame.playerseven == user.username
            ))).count()

        if DominionCount > maxCount:
            maxCount = DominionCount
            bestFriend = friend.fullname
        if CatanCount > maxCount:
            maxCount = CatanCount
            bestFriend = friend.fullname
        if LordsofWaterdeepCount > maxCount:
            maxCount = LordsofWaterdeepCount
            bestFriend = friend.fullname
        if CoupCount > maxCount:
            maxCount = CoupCount
            bestFriend = friend.fullname
        if LoveLetterCount > maxCount:
            maxCount = LoveLetterCount
            bestFriend = friend.fullname
        if MunchkinCount > maxCount:
            maxCount = MunchkinCount
            bestFriend = friend.fullname
        if TheMindCount > maxCount:
            maxCount = LoveLetterCount
            bestFriend = friend.fullname
        if JustOneCount > maxCount:
            maxCount = LoveLetterCount
            bestFriend = friend.fullname
        
    print(bestFriend)
    return bestFriend

        # DominionCount = db.session.query(DominionGame).filter(or_(
        #     DominionGame.winnerName == friend.fullname,
        #     DominionGame.secondName == friend.fullname,
        #     DominionGame.thirdName == friend.fullname,
        #     DominionGame.fourthName == friend.fullname,
        #     DominionGame.winnerName == friend.username,
        #     DominionGame.secondName == friend.username,
        #     DominionGame.thirdName == friend.username,
        #     DominionGame.fourthName == friend.username,
        #     DominionGame.winnerName == user.fullname,
        #     DominionGame.secondName == user.fullname,
        #     DominionGame.thirdName == user.fullname,
        #     DominionGame.fourthName == user.fullname,
        #     DominionGame.winnerName == user.username,
        #     DominionGame.secondName == user.username,
        #     DominionGame.thirdName == user.username,
        #     DominionGame.fourthName == user.username)).count()