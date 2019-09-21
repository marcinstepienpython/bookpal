import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('books.html')


if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)