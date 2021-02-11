from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  # return 'Hello Flask!!'
  return render_template('home.html')

# The route name does not need to match the function name
@app.route('/about')
def about():
  return 'This is a url shortener'