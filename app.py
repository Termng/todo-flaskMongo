from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)

# this is a mongodb database
db = client.flask_database

# this is a todos collection
todos = db.todos

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form['todoField']
        degree = request.form['degree']
        todos.insert_one({'todoField' : content, 'degree': degree })
        return redirect(url_for('home'))
    
    all_todos = todos.find()
    return render_template('home.html', todos=all_todos)

@app.post ('/<id>/del/')
def delete(id):
    todos.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)