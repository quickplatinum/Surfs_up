from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'When will we learn from our mistakes and conform'
app.run()