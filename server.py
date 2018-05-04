from flask import Flask, render_template, redirect, request, session
import math, datetime, random

app=Flask(__name__)
app.secret_key = 'DontForgetToSetASecretKey'

formDB=[
		{
		'value': 'Farm',
		'lowVal': 10,
		'highVal': 20
		},
		{
		'value': 'Cave',
		'lowVal': 5,
		'highVal': 10
		},
		{
		'value': 'House',
		'lowVal': 2,
		'highVal': 5
		},
		{
		'value': 'Casino',
		'lowVal': 0,
		'highVal': 50
		}
]


@app.route('/')
def landing():
	if 'yourGold' not in session:
		session['yourGold'] = 0
	if 'actions' not in session:
		session['actions'] = []
	print("session values ==>", session)
	return render_template('index.html', formDB = formDB, actions = session['actions'])

@app.route('/processMoney', methods=['POST'])
def processMoney():
	if request.form['building'] == 'Farm':
		gainLoss = "gain"
		goldNum = random.randrange(10,21)
	if request.form['building'] == 'Cave':
		gainLoss = "gain"
		goldNum = random.randrange(5,10)
	if request.form['building'] == 'House':
		gainLoss = "gain"
		goldNum = random.randrange(2,5)
	if request.form['building'] == 'Casino':
		goldNum = random.randrange(-50,50)
		if goldNum < 0:
			gainLoss = "loss"
		else:
			gainLoss = "gain"
	if session['yourGold'] < 0:
		gainLoss = "broke"

	session['yourGold'] += goldNum
	session['actions'].append({"credit":goldNum, "gainLoss":gainLoss, "building":request.form['building']})
	print(session['actions'])
	print(request.form)
	print("session values ==>", session)
	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)


