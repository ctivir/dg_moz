


# [Django](https://docs.djangoproject.com) Project
The aim is to list all Django Girls Workshops held in Mozambique 

## Table of contents

 - [Table of contents](#table-of-contents)
 - [Overview](#overview)
    - [Built with](#built-with)
      - [Requirements](#Requirements)
      - [Installation](#Installation)
    - [How to contribute](#how-to-contribute)
    - [Useful resources](#useful-resources)
 - [Acknowledgments](#acknowledgments)

## Overview

### Built with

- [Django](https://www.djangoproject.com/) - Python Web Framework

### Requirements

- Python (3.6, 3.7, 3.8, 3.9, 3.10, older)
- Django (2.2, 3.0, 3.1, 3.2, 4.0, older)

We highly recommend and only officially support the latest patch release of each Python and Django series.

### Installation

- Install using pip...

 1. pip install -r requirements.txt

## How to contribute

To contribute to this project you have to fork it and clone it.

`git clone https://github.com/ctivir/dg_moz.git` Clone project

After cloning it, in the project directory, run:

 1. `cd dg_moz` Get project folder
 2. `python3 -m venv env` create virtual env
 3. `source env/bin/activate` activate virtual env
 4. `./python manage.py createsuperuser` create superuser to have access to django admin
 5. `./manage.py makemigrations` create new migrations based on the changes you have made to your models.
 6. `./manage.py migrate` appy all migrations.
 7. `./manage.py runserver` to run the app in the development mode.
     Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

     The page will reload if you make edits.

## Useful resources

- [Django Documentation](https://docs.djangoproject.com)

## Acknowledgments
- [Cecilia](https://github.com/ctivir)
- [Ivo](https://github.com/naftalivo)
- [Euclesia](https://github.com/euclesiacadia)

