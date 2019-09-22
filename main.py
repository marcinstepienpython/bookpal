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


@app.route('/')
def home():
    return render_template('books.html', books=mongo.db.books.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
