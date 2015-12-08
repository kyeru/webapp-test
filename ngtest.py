from flask import Flask, render_template
#from flask.ext.triangle import Triangle

app = Flask(__name__)
#Triangle(app)

@app.route('/')
def default():
    return render_template('ngtest.html')

if __name__ == '__main__':
    app.run(debug = True)
