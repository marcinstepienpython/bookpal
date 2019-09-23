# bookpal

Book review and recommendation site.

repository: https://github.com/marcinstepienpython/bookpal
application is available here:

# Project goal

Application for book reviews and recommendation. User can add books, reviews, comments and vote for favorite titles. Available actions include Creating, Reading, Updating and Deleting records. Each book has a call-to-action button redirecting user to Amazon store, where purchase of the book is available. Each 'buying' link includes bookpal token enabling discounts and making money by referring users to Amazon (affiliate program).

## UX

THE LAYOUT:
The layout includes:

Main navigation:

- BookPal logo,
- Books => presenting all aded books
- Add a new book => user form for adding new books

Treding books:
This section presents up to four titles of books with highest increase of likes in the last week (functionality is not implemented yet).

Recently added books:
Section presenting books added in the last two weeks (functionality is not implemented yet).

Bestsellers:
Section presenting book(s) with the highest number of sold copies (functionality is not implemented yet).

Main goal of the UX design was to create a clean, well structured layout promoting (and selling) trending books and bestsellers. The page consists mostly of book covers which make it colorful and interesing, as book covers by default compete for user's attention.

USER SCENARIOS:
Available user scenarios:

- Searching books => user searches books on the main page (trending and recently added books)
- Creating/Updating/Deleting books => user can easily add books by filling the form.
- Adding comments => user can add comment about the book/review on each book details page.
- Upvoting => user can upvote books => stars

### Existing Features

- Creating/Updating/Deleting books
- Adding comments
- Upvoting ("Vote for this book") => each like (star) is an object with user name, which will enable reffering user to other books he/she might be interested in.
- Affiliate links for each book

### Features Left to Implement

- Algorithms for awarding stars (rating system) => limitation of voting by a single user (one vote)
- Algorithm for selection of trending books
- Algorithm for selecion of bestsellers

## Technologies Used

- [Bootstrap](https://getbootstrap.com/)

  - The project uses **Bootstrap** to simplify managing layout and CSS elements.

- [Google Fonts](https://fonts.google.com/)

  - The project uses **Google Fonts** to display beautiful and free fonts.

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation.

- [Fontawesome](https://fontawesome.com/)
  - The project uses **Fontawesome** for beautiful free icons.

The site has been created using:

- HTML
- CSS
- JavaScript
- Flask (flask, render_template, url_for, request, dnspython, redirect, PyMongo, bson.objectid )
- MongoDB + Atlas

## Database collection schema

- \_id: ObjectId
- title: String
- author: String
- cover: String
- teaser: String
- reviewer: String
- review: String
- comments: Array of Objects
- likes:Int32
- trending: Boolean
- book_of_the_month: Boolean
- hearts: Array of Objects

## Testing

Basic set-up:
Testing connection to mongo database. Exporting environment variables. Testing routes (no dead-ends)

Layout:
Testing site responsiveness:
Testing included Chrome, Firefox and Microsoft Edge. Site tested using Developer Tools for different mobile phones (Samsung, iPhone, tablets). Positive tests result with full responsiveness and behaviour on specific models. Responsive web design based on Boostrap grid system and flexbox.

Testing user scenarios:

- searching for books
- adding a new book => updating it and deleting.
- adding comments to different books
- upvoting books

## Deployment

The application has been deployed to Heroku server.

### Content

The application uses books descriptions from http://www.Wikipedia.com and http://www.amazon.com

### Media

The app uses several cover images from penguinrandomhouse.com:
"https://images2.penguinrandomhouse.com/cover/9781612198262"
"https://images2.penguinrandomhouse.com/cover/9780399180453"
"https://images2.penguinrandomhouse.com/cover/9780525655398"
"https://images4.penguinrandomhouse.com/cover/9780553385540"

### Acknowledgements

Codeinstitute https://codeinstitute.net
Corey Schafer https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
