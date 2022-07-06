APIs with django rest framework
Custom User Models and Model Managers in django
Token based Authentication
UUID's Advantages vs Disadvantages, How sudo primary keys solve this?
API testing with Pytest using Factories and Fixtures
Django Filtering, Signals, Admin Customization, Security.
Logging in Django.
Docker and Containerization, Shell scripts in Docker.
A sync task with celery and Redis
NGiNX for Server.
Make File.
React, Redux.


===========================================================================
-Set settings environment variables e.g secret_key, debug, and allowed_hosts in .env file.

-Import .env file and configure it in settings.

-Create apps change every app path in there apps.py file move to apps dir.

-In settings.py define new apps => INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

-configure settings.py for development, staging, and production

-configure postgres db in development settings.py

-make db env variables in .env

-split settings.py and configure database in development settings

-settup media and static files urls in base settings and urls.py

-configure development settings file path in wsgi.py

-LOGGING [Loggers, Handlers, Filters, Formatters] **

-LOGGERS [DEBUG, INFO, WARNING, ERROR, CRITICAL]

-HANDLERS [FileHandler, StreamHandler, SMTP Handler]

-FILTERS [Filter log messages from loggers to handlers]

-FORMATTERS [Format text for loggers]

-Abstract User vs Abstract Base user

- define custom user and superuser manager in users app managers.py file

-using UUIDs
    -safe and secure
    -obscure foreign key references
    -allow for horizontal partitioning in database without key collision or re keying concerns.

    *cause massive insert performance issues
    *no sort by id available

Therefor we implement a sudo primary key.

-define custom user model in models.py

-in settings give path of custom user model

-register custom user in django admin

-register custom user and useradmin in user app's admin.py

-settup psudo primary key and UUID model in apps>common>model

-make profile models in apps>profile>models

-use signals to ensure whenever a user is created a relevent profile is also created.
--create signals.py in apps>profile

-Created profiles, and profile ratings.

-for token based auth use djoser