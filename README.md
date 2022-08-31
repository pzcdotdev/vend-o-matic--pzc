# VEND-O-MATIC 

## Running the service
Prerequisites:
- make sure you have docker installed

Commands to run the service:
1. `cd /vend-o-matic--pzc/` 
1. `docker-compose up`

This will install poetry, download dependencies, run migrations, and start the service at `0.0.0.0/8000`

-------------

## Postman test API calls
You can find some handy Postman calls in `/vend-o-matic--pzc/Vend-O-Matic.postman_collection.json` 

-------------

## Running tests

Run tests using Django's default test runner:
1. `cd /vend-o-matic--pzc/vend-o-matic/`
1. `python manage.py test`

-------------

## If you run out of drinks...
Shut down the service, delete the sqlite database `db.sqlite`, then run `docker-compose up` again.

-------------
