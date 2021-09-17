# FantasticShop
FantasticShop is an example project with a couple of APIs
that represent an online shopping website. There are two
rolls of Admin and User, Admins can add/remove products
and track orders, Users can see products, add them to the
cart, and finally request for checking out.

## How to run
To run FantasticShop in development mode; Just use steps below:
1. Install python3.8.0, pip, virtualenv in your system.
3. Make development environment ready using commands below.

```bash
git clone https://github.com/arashmjr/FantasticShop && cd FantasticShop
virtualenv venv   # Create virtualenv named venv
venv\Scripts\activate # If You're On A Windows Machine
source venv/bin/activate # If You're On A Linux
pip install -r requirements.txt
install and configuration of postgresql using the following sections 
python manage.py makemigrations 
python manage.py migrate # Create database tables
```
4. Run app using python manage.py runserver

## django_postgresql
using postgresql database with django
## INSTALLATION
Install the postgresql database in your local computer first from the .exe file on the official site.

Install the postgresql package for python - psycopg2 using pip in virtualenv
## CONFIGURE

Create a new database using the postgresql command line.

CREATE DATABASE FantasticShop

Inside our django project settings.py, set the default database as the postgresql 
and set road database the the postgis like so,
```bash
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Shop',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',

    }
```
Just create models and run python manage.py makemigrations and python manage.py migrate commands, the new databases should work fine.

## Note 
If you think this repo need to have new usecase feel free to add an issue or send a pull request.

## Author
arashmjr, arash.mjr@gmail.com


