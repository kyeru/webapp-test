from flask import Flask, render_template
#from flask.ext.triangle import Triangle
from datetime import datetime

app = Flask(__name__)
#Triangle(app)

@app.route('/')
def default():
    return render_template('ngtest.html')

@app.route('/bs')
def bootstrap():
    timestamp = datetime.today()
    return render_template(
        'bootstrap_prac.html',
        timestamp = str(timestamp))

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
