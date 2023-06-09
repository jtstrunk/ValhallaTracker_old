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

@app.route('/Dominion')
def dominion():
    user = {'username': 'Joshua'}
    return render_template('dominion.html', title='Home', user=user)

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            player1 = request.form['Player1']
            player1Score = request.form['Player1_Score']
            player2 = request.form['Player2']
            player2Score = request.form['Player2_Score']
            with sqlite3.connect('brotha.db') as conn:
                c = conn.cursor()
                c.execute("SELECT MAX(game_id) + 1 FROM DominionGames")
                newGameID = c.fetchone()[0]
                print(newGameID)
                print("Being inserted")
                c.execute("INSERT INTO DominionGames (game_id, Player1Name, Player1Score, Player2Name, Player2Score) VALUES (?, ?, ?, ?, ?)", (newGameID, player1, player1Score, player2, player2Score))
                conn.commit()
        finally:
            return render_template('dominion.html', title='Home')
        
@app.route('/added', methods = ['GET'])
def added():
    with sqlite3.connect('brotha.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM DominionGames")
        c.execute("SELECT * from DominionGAMES WHERE game_id = 1")
        gameData = c.fetchall()
        print(gameData)

    return render_template('DominionOutput.html', title='Home', gameData=gameData)