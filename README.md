# Django simple form

## Local run of app

**Following steps assume Linux and Python 3.8.**

Create virtual environment 

    python -m venv path_to_env

Activate virtual environment
    
    . path_to_env/bin/activate
    
Install dependencies
    
    pip install -r requirements.txt
    
Create your Postgres database and export these environment variables:

     DB_NAME
     DB_USER
     DB_PASS
     DB_HOST
     DB_PORT

Generate and set SECRET_KEY

    export SECRET_KEY=$(openssl rand -base64 40)
   
Apply migrations

    python manage.py migrate
    
Create admin superuser

    python manage.py createsuperuser
  
Generate static files

    python3 manage.py collectstatic
    
Run application server
    
    gunicorn django_form.wsgi --log-file -