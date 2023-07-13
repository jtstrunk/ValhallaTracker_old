from app import app, db, User, friends, Date
from flask_login import UserMixin



# Create the database tables
with app.app_context():

    class basicGame(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, nullable=False)
        winnerName = db.Column(db.String(50), nullable=False)
        secondName = db.Column(db.String(50), nullable=False)
        thirdName = db.Column(db.String(50))
        game = db.Column(db.String(50))
        date = db.Column(Date)

    db.create_all()