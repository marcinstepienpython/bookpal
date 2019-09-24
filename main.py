import os
from flask import Flask, render_template, url_for,request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# DATABASE ENVIRONMENT

app.config['MONGO_DBNAME'] = "MSTEST"
pwd = os.environ['MONGO_DB_PASS']
app.config['MONGO_URI'] = "mongodb+srv://mstest:" + pwd + \
    "@mstest-okfns.mongodb.net/bookpal?retryWrites=true&w=majority"

mongo = PyMongo(app)

# ROUTES
# BOOK DETAILS
@app.route('/<book_id>')
def book_details(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('book_details.html', book=the_book)

# CREATING NEW BOOK
@app.route('/new_book')
def new_book():
    return render_template('new_book.html')

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

#UPDATING BOOK
@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('edit_book.html', book=the_book)

@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books
    books.update( {'_id': ObjectId(book_id)},
    {
        'title':request.form.get('title'),
        'author':request.form.get('author'),
        'cover': request.form.get('cover'),
        'teaser': request.form.get('teaser'),
        'reviewer':request.form.get('reviewer'),
        'review':request.form.get('review'),
        'likes':request.form.get('likes'),
        'trending':request.form.get('trending'),
        'book_of_the_month':request.form.get('book_of_the_month')
    })
    return redirect(url_for('book_details', book_id=book_id))

# UPVOTING
@app.route('/hearts/<book_id>', methods=['POST'])
def add_heart(book_id):
    books = mongo.db.books
    books.update({"_id": ObjectId(book_id)}, {"$push": {"hearts": {'heart':"userName"}}})
    
    return redirect(url_for('book_details', book_id=book_id))

# ADDING COMENTS
@app.route('/comments/<book_id>', methods=['POST'])
def add_comment(book_id):
    books = mongo.db.books
    books.update({"_id": ObjectId(book_id)}, {"$push": {"coments": {
        "name":request.form.get('name'),
        "comment":request.form.get('comment')}}})
    
    return redirect(url_for('book_details', book_id=book_id))

# DELETING BOOK
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('home'))

# MAIN PAGE
@app.route('/')
def home():
    return render_template('books.html',
                           books=mongo.db.books.find(),
                           recently_added=mongo.db.books.find(),
                           books_of_the_month=mongo.db.books.find({"book_of_the_month": True}))


# APP INITIALIZATION
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
