# library_management
This is a Library Management System built using Flask. It enables managing Books and Members while providing features like CRUD operations, search functionality for books by title or author, and token-based authentication to ensure secure access.

# Prerequisites

  To run this project, you need:

    1. Python 3.x (Ensure Python 3.6 or later is installed)
    2. A code editor like VSCode, PyCharm, or Sublime Text.
    3. Postman or curl for API testing.


# Run App.py file in command prompt.

# Features

1. CRUD actions for Books and Members: Add, Access, Modify, and Remove books and members.

2. Look for books by their title or author.

3. Token-driven authentication for safeguarded access to the API.

4. Page numbering for book listings, simplifying the management of extensive datasets.



# API Endpoints

Authentication: 

  1. POST /login: Description: Authenticates the user and returns a token for protected routes.

# Books CRUD Operations

GET /books: Description: Retrieves a list of all books (with pagination).
Headers: x-access-token: valid_token  

POST /books: Description: Adds a new book to the library.
Headers: x-access-token: valid_token


# Verification :

   The system employs authentication based on tokens. To verify your identity, submit a POST request to /login along with your credentials. You will obtain a token that must be added to the header of future requests. 

# Assumptions & Limitations: 
    1. In-memory storage: The application uses in-memory storage, so data is not persistent and will be lost when the server is restarted.
    2. No real user authentication: The token-based authentication system is a mock and does not involve real user credentials.
    3. Basic Pagination: Pagination is implemented for the /books route, but could be extended for other routes or to support more advanced pagination features.
