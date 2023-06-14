import sqlite3
# from flask import jsonify
# from flask import request

conn = sqlite3.connect('brotha.db')
c = conn.cursor()

# c.execute("""
#     CREATE TABLE CoupGames (
#     game_id integer PRIMARY KEY,
#     winnerName text NOT NULL, 
#     winnerCardsLeft text NOT NULL,
#     secondName text NOT NULL,
#     thirdName text,
#     fourthName text,
#     fifthName text,
#     sixthName text)""")
# print("Table made succsessfully")

# c.execute("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name")
# print(c.fetchall())

c.execute("INSERT INTO CoupGames (game_id, winnerName, winnerCardsLeft, secondName, thirdName, fourthName, fifthName, sixthName) VALUES ('13', 'Josh', '1','Lindsey', 'Connor', 'Larson', 'Wells', 'Tory')")
conn.commit()
c.execute("INSERT INTO CoupGames (game_id, winnerName, winnerCardsLeft, secondName, thirdName, fourthName, fifthName, sixthName) VALUES ('14', 'Wells', '2','Connor', 'Josh', 'Larson', 'Tory', 'Lindsey')")
conn.commit()
c.execute("INSERT INTO CoupGames (game_id, winnerName, winnerCardsLeft, secondName, thirdName, fourthName, fifthName, sixthName) VALUES ('15', 'Jim', '1', 'Harrison', 'Connor', 'Josh', 'Ethan', 'Jacob')")
conn.commit()
c.execute("INSERT INTO CoupGames (game_id, winnerName, winnerCardsLeft, secondName, thirdName, fourthName, fifthName, sixthName) VALUES ('16', 'Ethan', '2','Josh', 'Connor', 'Jim', 'Jacob', 'Harrison')")
conn.commit()

# c.execute("INSERT INTO CatanGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('1', 'Josh', '10', 'John', '8', 'Sam', '7', 'Stephan', '6')")
# conn.commit()
# c.execute("INSERT INTO CatanGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('2', 'Sam', '10', 'Josh', '9', 'John', '7', 'Stephan', '7')")
# conn.commit()
# c.execute("INSERT INTO CatanGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('4', 'Josh', '10', 'Nathan', '8', 'Stephan', '6', 'Ben', '5')")
# conn.commit()
# c.execute("INSERT INTO CatanGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('8', 'Heather', '10', 'Hayley', '9', 'Jessica', '9', 'Jayna', '8')")
# conn.commit()

# c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('3', 'Josh', '26', 'John', '20', 'David', '14', 'Stephan', '10')")
# conn.commit()
# c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('5', 'David', '30', 'Josh', '19', 'John', '16', 'Ethan', '15')")
# conn.commit()
# c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('6', 'John', '24', 'Josh', '22', 'Ethan', '18', 'Jim', '16')")
# conn.commit()
# c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES ('7', 'David', '32', 'Sam', '26', 'Josh', '25', 'Stephan', '16')")
# conn.commit()

# c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score) VALUES ('9', 'Jeff', '420', 'Bill', '69', 'Timmy', '25')")
# conn.commit()

# c.execute("DELETE FROM DominionGames")
# conn.commit()
# c.execute("DELETE FROM CatanGames")
# conn.commit()

# c.execute("SELECT MAX(game_id), Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score from CatanGAMES")
# print(c.fetchall())

# c.execute("SELECT MAX(game_id) + 1 FROM DominionGames")
# print(c.fetchone()[0])
# c.execute("SELECT game_id FROM DominionGames")


c.execute("SELECT * from CoupGames")
print(c.fetchall())
# c.execute("SELECT * from CatanGames")
# print(c.fetchall())
