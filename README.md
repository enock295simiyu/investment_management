# Management Investment Demo System

This is a Django Rest Framework (DRF) API for managing investment accounts that allows more than one user to belong to
an investment account it should also allow a user to belong to more than one investment account, with the following
requirements:

User Permissions: Extend the User and Django model permissions so that a user can have multiple investment accounts,
each with different levels of access:
Investment Account 1: The user should only have view rights and should not be able to make transactions.
Investment Account 2: The user should have full CRUD (Create, Read, Update, Delete) permissions.
Investment Account 3: The user should only be able to post transactions, but not view them.

## Setting up the project

* Clone the repository
* Navigate to the project directory and run the following commands:
* Ensure that you have python installed on your machine.

```shell
python --version
```

If you get an error, visit Python.org and download the latest version. When installing ensure python is added to your
PATH.

### Installing Requirements:

Run the following command to check if its installed:

```shell
pip install pipenv
```

This will install pipenv which is the tool we use to manage our dependencies.

```shell
pipenv install
```

This will install all the dependencies.

### Database:

The database used is SqlLite.

Running the following command to create the tables:

```shell
python manage.py migrate
```

This will create the tables in the database. You can also run the following command to create the superuser:

```shell
python manage.py createsuperuser
```

Running the server: If you received no errors, you can now run the server with the command bellow.

```shell
python manage.py runserver
```

You can now access the documentation of the application at http://localhost:8000/api/v1/docs/
