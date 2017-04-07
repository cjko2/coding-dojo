from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def renderIndex():
	name = 'Colin'
	return render_template('index.html', name=name)

app.run(debug=True)