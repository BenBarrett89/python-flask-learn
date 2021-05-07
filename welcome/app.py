#!python3

# specify which libraries and modules to use (don't import all)
from flask import Flask

# __name__ is something he doesn't explain
app = Flask(__name__)

# @ is a decorator (of the below function) - provide additional functionality to an existing function
@app.route('/')
def root():
  return 'This is my root page'

@app.route('/bob')
def bob():
  return 'Yo Bob! What\'s happening man?'

app.run()
