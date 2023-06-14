from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect
from flask import request
import sqlite3

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshua'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/showGames', methods=['GET'])
def showGames():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM DominionGames")
        Dominiondata = c.fetchall()
        print(Dominiondata)
        c.execute("SELECT * FROM CatanGames")
        Catandata = c.fetchall()
        print(Catandata)
        c.execute("SELECT * FROM LordsofWaterdeepGames")   
        LordsofWaterdeepdata = c.fetchall()
        print(LordsofWaterdeepdata)
        c.execute("SELECT * FROM CoupGames")   
        Coupdata = c.fetchall()
        print(Coupdata)
    return render_template('GameRecords.html', title='Home', Dominiondata=Dominiondata, Catandata=Catandata, LordsofWaterdeepdata=LordsofWaterdeepdata, Coupdata=Coupdata)

@app.route('/addGame', methods=['GET'])
def addGame():
    return render_template("addGame.html", title='Home')

@app.route('/Dominion', methods = ['GET'])
def Dominion():
    user = {'username': 'Joshua'}
    return render_template('Dominion.html', title='Home', user=user)

@app.route('/addDominion', methods = ['POST', 'GET'])
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
            with sqlite3.connect('brotha.db') as conn:
                c = conn.cursor()
                newGameID = findID()
                # c.execute("SELECT MAX(game_id) + 1 FROM DominionGames")
                # newGameID = c.fetchone()[0]
                print(newGameID)
                print("Being inserted")
                c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (newGameID, player1, player1Score, player2, player2Score, player3, player3Score, player4, player4Score))
                conn.commit()
                print("Inserted")
        finally:
            print("Redircting")
            return redirect("http://localhost:5000/DominionAdded")
        
@app.route('/DominionAdded', methods = ['GET'])
def DominionAdded():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM DominionGames")
        c.execute("SELECT MAX(game_id), Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score from DominionGAMES")
        gameData = c.fetchall()
        print(gameData)

    return render_template('DominionOutput.html', title='Home', gameData=gameData)

@app.route('/Catan', methods = ['GET'])
def Catan():
    user = {'username': 'Joshua'}
    return render_template('Catan.html', title='Home', user=user)

@app.route('/addCatan', methods = ['POST', 'GET'])
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
            with sqlite3.connect('brotha.db') as conn:
                c = conn.cursor()
                newGameID = findID()
                # c.execute("SELECT MAX(game_id) + 1 FROM CatanGames")
                # newGameID = c.fetchone()[0]
                print(newGameID)
                print("Being inserted")
                c.execute("INSERT INTO CatanGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (newGameID, player1, player1Score, player2, player2Score, player3, player3Score, player4, player4Score))
                conn.commit()
                print("Inserted")
        finally:
            print("Redircting")
            return redirect("http://localhost:5000/CatanAdded")
        
@app.route('/CatanAdded', methods = ['GET'])
def CatanAdded():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM CatanGames")
        c.execute("SELECT MAX(game_id), Player1Name, Player1Score, Player2Name, Player2Score, Player3Name, Player3Score, Player4Name, Player4Score from CatanGAMES")
        gameData = c.fetchall()
        print(gameData)

    return render_template('DominionOutput.html', title='Home', gameData=gameData)

@app.route('/LordsofWaterdeep', methods = ['GET'])
def LordsofWaterdeep():
    user = {'username': 'Joshua'}
    return render_template('LordsofWaterdeep.html', title='Home', user=user)

@app.route('/addLordsofWaterdeep', methods = ['POST', 'GET'])
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

            with sqlite3.connect('brotha.db') as conn:
                c = conn.cursor()
                newGameID = findID()
                # c.execute("SELECT MAX(game_id) + 1 FROM DominionGames")
                # newGameID = c.fetchone()[0]
                print(newGameID)
                print("Being inserted")
                c.execute("INSERT INTO LordsofWaterdeepGames (game_id, winnerName, winnerScore, secondName, secondScore, thirdName, thirdScore, fourthName, fourthScore, fifthName, fifthScore) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (newGameID, player1, player1Score, player2, player2Score, player3, player3Score, player4, player4Score, player5, player5Score))
                conn.commit()
                print("Inserted")
        finally:
            print("Redircting")
            return redirect("http://localhost:5000/LordsofWaterdeepAdded")
        
@app.route('/LordsofWaterdeepAdded', methods = ['GET'])
def LordsofWaterdeepAdded():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM LordsofWaterdeepGames")
        c.execute("SELECT MAX(game_id), winnerName, winnerScore, secondName, secondScore, thirdName, thirdScore, fourthName, fourthScore, fifthName, fifthScore from LordsofWaterdeepGames")
        gameData = c.fetchall()
        print(gameData)

    return render_template('LordsofWaterdeepOutput.html', title='Home', gameData=gameData)

@app.route('/hello')
def hello():
    print("help")
    return render_template('Coup.html')

@app.route('/Coup', methods = ['GET'])
def Coup():
    user = {'username': 'Joshua'}
    return render_template('Coup.html', title='Home', user=user)

@app.route('/addCoup', methods = ['POST', 'GET'])
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


            with sqlite3.connect('brotha.db') as conn:
                c = conn.cursor()
                newGameID = findID()
                # c.execute("SELECT MAX(game_id) + 1 FROM DominionGames")
                # newGameID = c.fetchone()[0]
                print(newGameID)
                print("Being inserted")
                c.execute("INSERT INTO CoupGames (game_id, winnerName, winnerCardsLeft, secondName, thirdName, fourthName, fifthName, sixthName) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (newGameID, cardsLeft, player1, player2, player3, player4, player5, player6))
                conn.commit()
                print("Inserted")
        finally:
            print("Redircting")
            return redirect("http://localhost:5000/CoupAdded")
        
@app.route('/CoupAdded', methods = ['GET'])
def CoupAdded():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM CoupGames")
        c.execute("SELECT MAX(game_id), winnerName, winnerCardsLeft, secondName, thirdName, fourthName, fifthName, sixthName from CoupGAMES")
        gameData = c.fetchall()
        print(gameData)

    return render_template('CoupOutput.html', title='Home', gameData=gameData)

def findID():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT MAX(game_id) + 1 FROM DominionGames")
        newGameID = c.fetchone()[0]
        c.execute("SELECT MAX(game_id) + 1 FROM CatanGames")
        tempGameID = c.fetchone()[0]
        if tempGameID > newGameID:
            newGameID = tempGameID
        c.execute("SELECT MAX(game_id) + 1 FROM LordsofWaterdeepGames")
        tempGameID = c.fetchone()[0]
        if tempGameID > newGameID:
            newGameID = tempGameID
    
    return newGameID