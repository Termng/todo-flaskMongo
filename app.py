from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

# this is a mongodb database
db = client.flask_database

# this is a todos collection
todos = db.todos

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)