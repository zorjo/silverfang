# Silverfang

Silverfang is a Django Rest Framework (DRF) based API built with PostgreSQL. It provides a CRUD interface for managing notes, with authenticated users, rate limiting, and search functionality.

## Table of Contents

- [Installation](#installation)
   - [Database Setup](#database-setup)
   - [Python Setup](#python-setup)
- [Features](#features)
- [Usage](#usage)
- [Rate Limiting](#rate-limiting)
- [Search Functionality](#search-functionality)
- [Authenticated Users](#authenticated-users)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the Silverfang API, you need to have Python, Django, and PostgreSQL installed on your machine. Follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/silverfang.git`
2. Navigate to the project directory: `cd silverfang`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the requirements: `pip install -r requirements.txt`
6. Run migrations: `python manage.py makemigrations && python manage.py migrate`
7. Start the server: `python manage.py runserver`

### Database Setup

please update `silverfang/.env` file to access with your database credentials,

### Python Setup

```
pip -r requirements.txt
django manage.py migrate
django manage.py runserver
```

## Features

- CRUD API of notes
- Authenticated users
- Rate limiting
- Search functionality

## Usage

### Hello World Endpoint

This endpoint returns a simple 'Hello, World!' message.

**Endpoint:** `/api/hello/`

**Method:** GET

**Response:** ` { "message": "Hello, World!" }`


### Create Note Endpoint

This endpoint creates a new note for the authenticated user.

**Endpoint:** `/api/notes/create/`

**Method:** POST

**Headers:** Authorization: Token <your_auth_token>

### List all Notes Endpoint

This endpoint all the notes the authenticated user.

**Endpoint:** `/api/notes/`

**Method:** GET

**Headers:** Authorization: Token <your_auth_token>

### Register User Endpoint

This endpoint allows any user to register.

**Endpoint:** `/api/auth/signup/`

**Method:** POST

**Body:** 'username,password'

### Obtain Token Endpoint

This endpoint allows any user to obtain their auth token

**Endpoint:** `/api/auth/token/`

**Method:** POST

**Body:** 'username,password'


### Search Endpoint

This endpoint searches for notes by a query string for the authenticated user.

**Endpoint:** `api/notes/search/?q={query}`

**Method:** GET

**Headers:** Authorization: Token <your_auth_token>

### Note Editing

This endpoint allows viewing, deleting, and updating a specific note for the authenticated user.

**Endpoint:** `/api/notes/{id}`

**Method:** GET,DELETE,PUT

**Headers:** Authorization: Token <your_auth_token>

## Testing
The tests for this project can be found in the `notes/tests.py` file, as well as in the `notes/test_views.py` and `notes/test_models.py` modules.

## License

MIT License


## Rate Limiting 
We have utilized rest_framework to throttle the api globally for anonymous, registered users. 

## Project Structure 
```

│   .gitignore
│   db.sqlite3
│   manage.py
│   README.md
│   requirements.txt
│
├───notes
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   serializers.py
│   │   tests.py
│   │   test_models.py
│   │   test_views.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│    ───migrations
│      │   0001_initial.py
│      │   0002_note_author.py
│      │   0003_remove_note_author_remove_note_created_at_and_more.py
│      │   0004_remove_note_search_vector_alter_note_user.py
│      │   0005_note_search_vector.py
│      │   __init__.py
│      │
│      └───__pycache__
│              0001_initial.cpython-311.pyc
│              0002_note_author.cpython-311.pyc
│              0003_remove_note_author_remove_note_created_at_and_more.cpython-311.pyc
│              0004_remove_note_search_vector_alter_note_user.cpython-311.pyc
│              0005_note_search_vector.cpython-311.pyc
│              __init__.cpython-311.pyc
│   
└───silverfang
    │   .env
    │   asgi.py
    │   settings.py
    │   urls.py
    │   views.py
    │   wsgi.py
    │   __init__.py

```