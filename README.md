# Flask Starter

It is a Flask application starter.

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)

## Installation
To get started with this Flask application starter, clone this repository, setup virtual enviroment and install the dependencies:
```console
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Then create a `.env` file and adjust environment variables.
```
SECRET_KEY=mysupersecretkeyistoolongtoremember
```
> **Note:** This is only an example. Use a really strong key in production.

Next create the tables in the development SQLite database from the models. For this, Alembic is used.
```console
flask db upgrade
```
## Usage
After installation you can run the application using:
```console
flask run
```
This will start the development server at http://localhost:5000.
