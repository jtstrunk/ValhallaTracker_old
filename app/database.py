import sqlite3
# from flask import jsonify
# from flask import request

conn = sqlite3.connect('cards.db')
c = conn.cursor()

# c.execute("""
#     CREATE TABLE DominionGames (
#     game_id integer PRIMARY KEY,
#     Player1Name text NOT NULL, 
#     Player1Score text NOT NULL,
#     Player2Name text NOT NULL,
#     Player2Score text NOT NULL,
#     Player3Name text,
#     Player3Score text,
#     Player4Name text,
#     Player4Score text)""")
# print("Table made succsessfully")

#c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score) VALUES ('1', 'Josh', '10', 'John', '8')")

c.execute("SELECT * FROM DominionGames")
print(c.fetchall())
