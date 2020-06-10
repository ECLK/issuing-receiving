# issuing-receiving
![Build](https://github.com/ECLK/issuing-receiving/workflows/Node.js%20CI/badge.svg)

# Getting Started

## Frontend
Go to the frontend directory.

`cd frontend`

Install the dependencies

`npm install`

## Backend
Backend uses pipenv to manage dependencies.
Install pipenv by typing

`pip install pipenv`

Then go to the backend directory

`cd backend`

Activate virtual environment

`pipenv shell`

Install the depependencies

`pipenv install`

# Starting the dev environment

## Frontend
`npm start`

## Backend

Create admin user

`python manage.py createsuperuser`

Insert credentials

Migrate db

`python manage.py migrate`

Start server

`python manage.py runserver`


