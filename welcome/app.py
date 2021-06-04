#!python3

# specify which libraries and modules to use (don't import all)
from flask import Flask, request, render_template

# __name__ is something he doesn't explain
app = Flask(__name__)

# @ is a decorator (of the below function) - provide additional functionality to an existing function
@app.route('/')
def root():
  return render_template("index.html")

@app.route('/bob')
def bob():
  return 'Yo Bob! What\'s happening man?'

# methods can be provided in another argument
@app.route('/method', methods=['GET', 'POST'])
def method():
  if request.method == 'POST':
    return "You've used a POST request"
  else:
    return "I reckon you're probably using a GET request!"

app.run()
