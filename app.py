from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def intro():
    return render_template('./home.html')    

@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!</h1>'.format(name)

@app.route('/home')
def home():
    return render_template('home.html')
 
@app.route('/next')
def next():
    return render_template('option.html')

if(__name__=='__main__'):
    app.run()