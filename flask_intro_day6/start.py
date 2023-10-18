import random
from flask import Flask

app = Flask(__name__)

r=random.randint(0,9)

@app.route("/")
def hello_world():
    return "<p>Guess number (0-9)</p>" \
    '<img src="https://media.giphy.com/media/dwI09ZWZ93gIt7uhQm/giphy.gif" alt="gif">'

@app.route("/bhai")
def bye():
    return "<p>Hello, Bhai!</p>"

#@app.route("/number/<num>")
#def no(num):
 #   return f"Number:{num}"

@app.route('/number/<int:Number>')
def number(Number):
    if Number == r:
        return f'<h2>Correct Guess!<h2> : {str(Number)}'\
    '<img src="https://media.giphy.com/media/b1w2N3j1u6cb9TcPrg/giphy.gif" alt="gif">'
    elif Number>r:
       return f'<h2>Guessed too high<h2>'\
    '<img src="https://media.giphy.com/media/xO4LHmO7ISBu42NQhW/giphy.gif" alt="gif">'
    else:
        return '<h2>Guessed too low<h2>'\
    '<img src="https://media.giphy.com/media/xO4LHmO7ISBu42NQhW/giphy.gif" alt="gif">'

if __name__=="__main__":
    app.run(debug=True)
    