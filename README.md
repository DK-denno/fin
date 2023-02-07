# [FINTECH](https://instadk.herokuapp.com)
#### By **[Dennis Kamau]**


## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3 or higher
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/DK-denno/fin.git fin && cd fin`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE school;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'school'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open browser on `localhost:8000`

### Create a super user Account (System Admin)
```bash
python3 manage.py createsuper and follow the prompts
```
Open browser on `localhost:8000/admin`

## Known bugs
The UI might not be the best but functionality is okaaay

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Postgresql

## Support and contact details
Contact me on dennisveer27@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Dennis Kamau**
