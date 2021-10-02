from flask import Flask, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=True)