from app import app, db,  friends, Date
from flask_login import UserMixin



# Create the database tables
with app.app_context():

    # userFavorites = db.Table('userFavorites',
    #     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    #     db.Column('game_id', db.Integer, db.ForeignKey('supported_games.id'))
    # )

    # class User(UserMixin, db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     fullname = db.Column(db.String(50), nullable=False)
    #     username = db.Column(db.String(15), nullable=False, unique=True)
    #     email = db.Column(db.String(50), nullable=False, unique=True)
    #     password = db.Column(db.String(80), nullable=False)

    #     favorites = db.relationship('SupportedGames', secondary=userFavorites, backref='favoritedby')

    #     friends = db.relationship('User', secondary=friends,
    #                             primaryjoin=(friends.c.user_id == id),
    #                             secondaryjoin=(friends.c.friend_id == id),
    #                             backref=db.backref('friend_of', lazy='dynamic'),
    #                             lazy='dynamic')
        
    # class SupportedGames(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     gameName = db.Column(db.String(50))
    #     numPlayers = db.Column(db.String(50))
        
        

    db.create_all()