from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): #needs to be right under the app line
	return render_template('index.html')

@app.route('/about')
def about(): #needs to be right under the app line
	return render_template('about.html')

app.run(debug=True)