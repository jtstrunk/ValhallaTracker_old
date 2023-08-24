# from app import app, db
# from flask_login import UserMixin



# # Create the database tables
# with app.app_context():

#     class MagicTheGatheringGame(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         game_id = db.Column(db.Integer, nullable=False)
#         winnerName = db.Column(db.String(50), nullable=False)
#         winnerColor = db.Column(db.String(50), nullable=False)
#         winnerKills = db.Column(db.Integer)
#         winnerDeck = db.Column(db.String(50))
#         secondName = db.Column(db.String(50), nullable=False)
#         secondColor = db.Column(db.String(50), nullable=False)
#         secondKills = db.Column(db.Integer)
#         secondDeck = db.Column(db.String(50))
#         thirdName = db.Column(db.String(50))
#         thirdColor = db.Column(db.String(50))
#         thirdKills = db.Column(db.Integer)
#         thirdDeck = db.Column(db.String(50))
#         fourthName = db.Column(db.String(50))
#         fourthColor = db.Column(db.String(50))
#         fourthKills = db.Column(db.Integer)
#         fourthDeck = db.Column(db.String(50))
#         fifthName = db.Column(db.String(50))
#         fifthColor = db.Column(db.String(50))
#         fifthKills = db.Column(db.Integer)
#         fifthDeck = db.Column(db.String(50))
#         date = db.Column(db.Date)

#     db.create_all()