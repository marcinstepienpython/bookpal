import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "MSTEST"
pwd = os.environ['MONGO_DB_PASS']
app.config['MONGO_URI'] = "mongodb+srv://mstest:" + pwd + \
    "@mstest-okfns.mongodb.net/bookpal?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/<book_id>')
def book_details(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('book_details.html', book = the_book)

@app.route('/')
def home():
    return render_template('books.html', 
    books=mongo.db.books.find(), 
    recently_added=mongo.db.books.find(), 
    books_of_the_month=mongo.db.books.find({"book_of_the_month": True}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
