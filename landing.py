from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secret103048580e8w7'

# THE DEFAULT LANDING PAGE
@app.route("/")
def landing():
	if 'names' not in session:
		session['names']=[]
	if 'emails' not in session:
		session['emails']=[]

	return render_template('index.html', names=session['names'], emails=session['emails'])

# NINJAS PAGE
@app.route("/ninjas")
def ninjaspage():
	return render_template('ninjas.html')

#THE HIDDEN PAGE WHERE THE DATA GETS POSTED TO
@app.route("/process", methods=["POST"])
def processform():
	newname = request.form['new_name']
	newemail = request.form['new_email']

	list_of_names = session['names']
	list_of_names.append(newname)
	session['names'] = list_of_names

	list_of_emails = session['emails']
	list_of_emails.append(newemail)
	session['emails'] = list_of_emails

	return redirect('/')
app.run(debug=True)