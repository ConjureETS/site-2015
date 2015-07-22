# Readme #

Official conjure website repository

## Python Version ##
V2.7.6

## System dependencies ##
Python, PIP

To install other dependencies :
```
pip install -r requirements.txt
```

## Databsae configuration ##
If you don't have the database yet initialize it with :
``` ./manage.py syncdb ```

If you need to apply some migrations to your existing database :
``` ./manage.py migrate [appname]```

If you change data model, don't forget to create the migration :
``` ./manage.py makemigrations [appname] ```

## To run the server locally ##
``` ./manage.py runserver ```

## Tests ##
To run tests locally just run 
``` ./manage test ```
or if you want to test the whole server
``` ./manage testserver ```

## Deployement instructions ##
Coming soon...
